from tkinter import *
from PIL import ImageTk, Image
import sys
from io import StringIO
import contextlib
import sqlite3
from tkinter import messagebox

# Configuration of the main tkinter window 
root = Tk()
root.title("PyMaster")
root.iconbitmap('disneyland.ico')
root.geometry("2000x2000")

# Setting the Background image in main window
filename = PhotoImage(file="poster.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Enter function : called from main window to check authorization locally
def Enter(id, pwd):
    # Connect to the database
    conn = sqlite3.connect('data_book.db')

    # Create cursor
    c = conn.cursor()

    # Check into table
    c.execute("SELECT*, oid FROM addresses")
    recs = c.fetchall()
    flag = 0

    # Reading records from table and checking authorization
    for rec in recs:
        if (pwd == rec[1]) and (id == rec[0]):
                flag = 1
                break
    # If credentials are valid then open new window
    if flag == 1:
        
        # New window configuration
        et = Toplevel()
        et.title("PyMaster")
        et.iconbitmap('disneyland.ico')
        et.configure(bg="Pink")
        et.geometry("2000x2000")

        # Select Function : called from next window to select the topic to learn 
        def Select():
            # Recieving option from user
            res = character.get()
            
            # 1st Choice of Radio Button
            if int(res) == 1:
                global i
                global s2
                global txt
                global btn1
                global btn2
                global btn3
                global btn4
                i = 0
                
                # Labels 
                lblm = Label(et, background="skyblue", padx=10, pady=10, text="Strings in Python3 ",
                             font=("Helvetica", 30))
                lblm.place(x=950, y=100, anchor="center")
                
                s1 = Label(et, background="skyblue", width=300, height=50,
                           text="In Python, Strings are arrays of bytes representing" +
                                " Unicode characters. However, Python does not have a " +
                                "character data type, a single character is simply a " +
                                "string with a length of 1. Square brackets can be used " +
                                "to access elements of the string. " +
                                "Strings in Python can be created using single quotes " +
                                "or double quotes or even triple quotes. " +
                                "\nRun the Follwing Codes one by one !!",
                           font=("Helvetica", 15), wraplength=1100)
                s1.place(x=670, y=270, anchor="center", relheight=0.2)
                
                # Run Function to run the code and get the output 
                def Run(code):
                    st = ""
                    @contextlib.contextmanager
                    def stdoutIO(stdout=None):
                        # Passing the current output of system to variable 'old'
                        old = sys.stdout
                        
                        # If nothing is passed as new outpt then an empty string is created as new output
                        if stdout is None:
                            stdout = StringIO()
                        # The new output is stored
                        sys.stdout = stdout
                        # Yielding the new output as string
                        yield stdout
                        # Returning the original ouput to system
                        sys.stdout = old
                        
                    # Using the stdIO function to produce output as string
                    with stdoutIO() as s:
                        try:
                            # Passing the output to s, if runs successfully returns output 
                            exec(code)
                            
                        except:
                            # For exception handling returns message Check the code
                            print("Check the code!!")
                            
                    # Storing yielded value of output in 
                    st = s.getvalue()

                    # Label for final output
                    global lbl
                    lbl = Label(et, text="Output : \n" + st, font=("Helvetica", 10), wraplength=500)
                    lbl.place(x=950, y=500, anchor="center")
                
                # Refresh1 Function : called from new window after topic selection, to refresh the whole window     
                def Ref1():
                    s2.destroy()
                    txt.destroy()
                    btn1.destroy()
                    btn2.destroy()
                    btn3.destroy()
                    btn4.destroy()
                    btn5.destroy()
                    
                # Refresh2 Function : called from new window to refresh the output of code
                def Ref2():
                    lbl.destroy()

                # Backtohome Function : called from new window to return to main window
                def Backtohm():
                    et.destroy()

                # Change Function : called from new window to traverse through the various example codes with index number
                def Change(i):
                    Ref1()
                    
                    # When reaching the first example code
                    if i == 0:
                        # Labels and Buttons
                        s2 = Label(et, padx=10, pady=10, text="Creating a String with single Quotes  :Code "+str(i+1)+" of 3",
                                   font=("Helvetica", 20))
                        s2.place(x=650, y=370, anchor="center")

                        txt = Text(et, font=("Helvetica", 10), height=10)
                        txt.insert("1.0", r"""String1 = 'Welcome to the World of Python'""" + "\n"
                                           r"""print("String with the use of Single Quotes: ")""" +
                                           "\n" + r"""print(String1)""")

                        txt.place(x=300, y=500, anchor="center")

                        btn1 = Button(et, text="Run", width=20, height=2, command=lambda: Run(txt.get("1.0", "end-1c")))
                        btn1.configure(font=("Helvetica", 10))
                        btn1.place(x=700, y=450, anchor="center")

                        btn2 = Button(et, text="REFRESH", width=20, height=2, command=Ref2)
                        btn2.configure(font=("Helvetica", 10))
                        btn2.place(x=700, y=500, anchor="center")

                        btn3 = Button(et, text="BACK TO HOMESCREEN", width=20, height=2, command=Backtohm)
                        btn3.configure(font=("Helvetica", 10))
                        btn3.place(x=700, y=550, anchor="center")

                        btn4 = Button(et, text="NEXT", padx=15, pady=10, command=lambda: Change(i+1))
                        btn4.configure(font=("Helvetica", 10))
                        btn4.place(x=650, y=600, anchor="center")

                        btn5 = Button(et, text="BACK", padx=15, pady=10, state=DISABLED)
                        btn5.configure(font=("Helvetica", 10))
                        btn5.place(x=750, y=600, anchor="center")
                        
                    # When reaching the second example code
                    if i == 1:
                        # Labels and Buttons
                        s2 = Label(et, padx=10, pady=10, text="Creating a String with double Quotes  :Code "+str(i+1)+" of 3",
                                   font=("Helvetica", 20))
                        s2.place(x=650, y=370, anchor="center")

                        txt = Text(et, font=("Helvetica", 10), height=10)
                        txt.insert("1.0", r"""String2 = "I'm a Python Developer" """ + "\n"
                                           r"""print("\nString with the use of Double Quotes: ") """ +
                                           "\n" + r"""print(String2)""")

                        txt.place(x=300, y=500, anchor="center")

                        btn1 = Button(et, text="Run", width=20, height=2, command=lambda: Run(txt.get("1.0", "end-1c")))
                        btn1.configure(font=("Helvetica", 10))
                        btn1.place(x=700, y=450, anchor="center")

                        btn2 = Button(et, text="REFRESH", width=20, height=2, command=Ref2)
                        btn2.configure(font=("Helvetica", 10))
                        btn2.place(x=700, y=500, anchor="center")

                        btn3 = Button(et, text="BACK TO HOMESCREEN", width=20, height=2, command=Backtohm)
                        btn3.configure(font=("Helvetica", 10))
                        btn3.place(x=700, y=550, anchor="center")

                        btn4 = Button(et, text="NEXT", padx=15, pady=10, command=lambda: Change(i + 1))
                        btn4.configure(font=("Helvetica", 10))
                        btn4.place(x=650, y=600, anchor="center")

                        btn5 = Button(et, text="BACK", padx=15, pady=10, command=lambda: Change(i - 1))
                        btn5.configure(font=("Helvetica", 10))
                        btn5.place(x=750, y=600, anchor="center")
                        
                    # When reaching the third example code
                    if i == 2:
                        # Labels and Buttons
                        s2 = Label(et, padx=10, pady=10, text="Creating a String with triple Quotes  :Code "+str(i+1)+" of 3",
                                   font=("Helvetica", 20))
                        s2.place(x=650, y=370, anchor="center")

                        txt = Text(et, font=("Helvetica", 10), height=10)
                        txt.insert("1.0", r"""String3 = '''Geeks """+"\n"+r"""For """+"\n"+"""Life'''""" + "\n"
                                          r"""print("\nString with the use of Double Quotes: ") """ +
                                          "\n" + r"""print(String2)""")

                        txt.place(x=300, y=500, anchor="center")

                        btn1 = Button(et, text="Run", width=20, height=2, command=lambda: Run(txt.get("1.0", "end-1c")))
                        btn1.configure(font=("Helvetica", 10))
                        btn1.place(x=700, y=450, anchor="center")

                        btn2 = Button(et, text="REFRESH", width=20, height=2, command=Ref2)
                        btn2.configure(font=("Helvetica", 10))
                        btn2.place(x=700, y=500, anchor="center")

                        btn3 = Button(et, text="BACK TO HOMESCREEN", width=20, height=2, command=Backtohm)
                        btn3.configure(font=("Helvetica", 10))
                        btn3.place(x=700, y=550, anchor="center")

                        btn4 = Button(et, text="NEXT", padx=15, pady=10, state=DISABLED)
                        btn4.configure(font=("Helvetica", 10))
                        btn4.place(x=650, y=600, anchor="center")

                        btn5 = Button(et, text="BACK", padx=15, pady=10, command=lambda: Change(i - 1))
                        btn5.configure(font=("Helvetica", 10))
                        btn5.place(x=750, y=600, anchor="center")

                  
                # The very first view after selecting topic , i.e, 1st example code
                # Labels and Buttons
                s2 = Label(et, padx=10, pady=10, text="Creating a String with single Quotes  : Code "+str(i+1)+" of 3",
                           font=("Helvetica", 20))
                s2.place(x=650, y=370, anchor="center")

                txt = Text(et, font=("Helvetica", 10), height=10)
                txt.insert(INSERT, r"""String1 = 'Welcome to the World of Python'""" + "\n"
                            r"""print("String with the use of Single Quotes: ")""" +
                           "\n" + r"""print(String1)""")

                txt.place(x=300, y=500, anchor="center")

                btn1 = Button(et, text="Run", width=20, height=2, command=lambda: Run(txt.get("1.0", "end-1c")))
                btn1.configure(font=("Helvetica", 10))
                btn1.place(x=700, y=450, anchor="center")

                btn2 = Button(et, text="REFRESH", width=20, height=2, command=Ref2)
                btn2.configure(font=("Helvetica", 10))
                btn2.place(x=700, y=500, anchor="center")

                btn3 = Button(et, text="BACK TO HOMESCREEN", width=20, height=2, command=Backtohm)
                btn3.configure(font=("Helvetica", 10))
                btn3.place(x=700, y=550, anchor="center")

                btn4 = Button(et, text="NEXT", padx=15, pady=10, command=lambda: Change(i + 1))
                btn4.configure(font=("Helvetica", 10))
                btn4.place(x=650, y=600, anchor="center")

                btn5 = Button(et, text="BACK", padx=15, pady=10, state=DISABLED)
                btn5.configure(font=("Helvetica", 10))
                btn5.place(x=750, y=600, anchor="center")

        
        # The very first view in new window to select topic for learning
        labl1 = Label(et, text="Choose topic : ", padx=20, pady=20)
        labl1.configure(font=("Helvetica", 30, "bold italic"))
        labl1.place(x=200, y=100, anchor="center")

        # Defining the topics
        MODES = [
            ("Strings", "1"),
        ]

        # Creating a Stringvar to store selected option
        character = StringVar()
        character.set("1")
        x, y = 400, 50
        # Loop to put radiobuttons on screen
        for text, mode in MODES:
            rd = Radiobutton(et, text=text, variable=character, value=mode)
            rd.configure(font=("Helvetica", 20, "bold italic"))
            rd.place(x=x, y=y)
            y += 50

        # Button to select
        btn = Button(et, text="Select", width=15, command=Select)
        btn.configure(font=("Helvetica", 20, "bold italic"))
        btn.place(x=400, y=120)

        et.mainloop()

    # In case of invalid credentials popup warning message
    else:
        # defining warning popup window with title "Invalid!!", and message = "Invalid Credentials" 
        response = messagebox.showwarning("Invalid!!", "Invalid Credentials")

# User Function : called from main window to update users in database
def user():
    # Configuring the manage user window
    root2 = Tk()
    root2.title("Users")
    root2.iconbitmap("disneyland.ico")
    root2.geometry("500x500")

    # DataBases

    # Connect to database
    conn = sqlite3.connect('data_book.db')

    # Create cursor
    c = conn.cursor()

    # Edit Function : Called from the update function on manage user window to edit information of existing users
    def edit():
        # Connect to databas
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        rid = del_box.get()
        
        # Updating information in table
        c.execute("""UPDATE addresses SET

            idt = :id,
            pwdt = :pwd

            WHERE oid = :oid""",
                  {
                      'id': ide.get(),
                      'pwd': pwde.get(),

                      'oid': rid
                  })

        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()
        ed.destroy()

    # Update Function : Called from the manage user window to edit information of existing users
    def update():
        global ed
        ed = Tk()
        ed.title("Update Record")
        ed.iconbitmap("disneyland.ico")
        ed.geometry("500x500")

        # Connect to database
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        rid = del_box.get()
        # Fetching information from table
        c.execute("SELECT* FROM addresses WHERE oid=" + rid)
        recs = c.fetchall()

        # Create Global
        global ide
        global pwde

        # Create Text Boxes
        ide = Entry(ed, width=30)
        ide.grid(row=0, column=1, padx=20)

        pwde = Entry(ed, width=30)
        pwde.grid(row=1, column=1, padx=20)

        # Create box labels
        id_lbl = Label(ed, text="ID : ", width=30)
        id_lbl.grid(row=0, column=0, padx=20)

        pwd_lbl = Label(ed, text="Password : ", width=30)
        pwd_lbl.grid(row=1, column=0, padx=20)

        del_lbl = Label(ed, text="Select Record no : ")
        del_lbl.grid(row=9, column=0)

        # Loop through results
        for rec in recs:
            ide.insert(0, rec[0])
            pwde.insert(0, rec[1])

        # Create Save Btn
        s_btn = Button(ed, text="Save", command=edit)
        s_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=137)
   
    # Delete Function : Called from the manage user window to delete information of existing users
    def delete():
        # Create a database or connect to one
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        # Deleting information from table
        c.execute("DELETE from addresses WHERE oid=" + del_box.get())
        del_box.delete(0, END)

        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()

    # Submit Function : Called from the manage user window to add information of new users
    def Submit():
        # Create a database or connect to one
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        # Insert into table
        c.execute("""INSERT INTO addresses VALUES (:id, :pwd)""",
                  {
                      'id': id.get(),
                      'pwd': pwd.get()
                  })

        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()

        # clear TextBoxes
        id.delete(0, END)
        pwd.delete(0, END) 
    
    # Show Function : Called from the manage user window to show the id and Sr no. of existing users
    def show():
        # Connect to database
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        # Fetching information from table
        c.execute("SELECT*, oid FROM addresses")
        recs = c.fetchall()
        # print(recs)

        # Loop through records
        p = ""
        for rec in recs:
            p += "    Sr. No : " + str(rec[2]) + "    ID : " + str(rec[0]) + "\n\n "

        q_lbl = Label(root2, text=p)
        q_lbl.grid(row=14, column=0, columnspan=2)

        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()

    
    # View Configuration of Manage user window
    # Create Text Boxes
    id = Entry(root2, width=30)
    id.grid(row=0, column=1, padx=20)

    pwd = Entry(root2, width=30)
    pwd.grid(row=1, column=1, padx=20)

    del_box = Entry(root2, width=30)
    del_box.grid(row=9, column=1)

    # Create box labels
    id_lbl = Label(root2, text="ID : ", width=30)
    id_lbl.grid(row=0, column=0, padx=20)

    pwd_lbl = Label(root2, text="Password : ", width=30)
    pwd_lbl.grid(row=1, column=0, padx=20)

    del_lbl = Label(root2, text="Select Record no. : ")
    del_lbl.grid(row=9, column=0)

    # Create Query Button
    q_btn = Button(root2, text="Show Records", command=show)
    q_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Create Submit Btn

    submit_btn = Button(root2, text="Add Data", command=Submit)
    submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    # Create Delete Btn

    del_btn = Button(root2, text="Delete Record", command=delete)
    del_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

    # Create Edit Btn
    ed_btn = Button(root2, text="Update Record", command=update)
    ed_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


# View Configuration of main window
# Welcome msg
l1 = Label(root, padx=30, text="Welcome  To  PyMaster !", font=("Helvetica", 50))
l1.place(x=800, y=100, anchor="center")

# Labels
# User ID
id_lbl = Label(root, padx=20, text="Enter User ID : ", font=("Helvetica", 15))
id_lbl.place(x=600, y=550, anchor="center")

pwd_lbl = Label(root, padx=10, text="Enter Password : ", font=("Helvetica", 15))
pwd_lbl.place(x=600, y=600, anchor="center")

# Entry
id_ent = Entry(root, width=20, background="Skyblue", borderwidth=2)
id_ent.configure(font=("Helvetica", 15))
id_ent.place(x=800, y=550, anchor="center")

pwd_ent = Entry(root, width=20, background="Skyblue", borderwidth=2)
pwd_ent.configure(font=("Helvetica", 15))
pwd_ent.place(x=800, y=600, anchor="center")

#Button
btn1 = Button(root, text="Enter", borderwidth=0, width=20, padx=1, pady=1, command=lambda: Enter(id_ent.get(), pwd_ent.get()))
btn1.configure(font=("Helvetica", 15))
btn1.place(x=680, y=640, anchor="center")

btn2 = Button(root, text="Manage Users", borderwidth=0, width=20, padx=1, pady=1, command=user)
btn2.configure(font=("Helvetica", 15))
btn2.place(x=680, y=680, anchor="center")

root.mainloop()
