from tkinter import *
from PIL import ImageTk, Image
import sys
from io import StringIO
import contextlib
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("PyMaster")
root.iconbitmap('disneyland.ico')
root.geometry("2000x2000")

filename = PhotoImage(file="poster.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def Enter(id, pwd):
    conn = sqlite3.connect('data_book.db')

    # Create cursor
    c = conn.cursor()

    # Check into table
    c.execute("SELECT*, oid FROM addresses")
    recs = c.fetchall()
    flag = 0

    for rec in recs:
        if (pwd == rec[1]) and (id == rec[0]):
                flag = 1
                break
    if flag == 1:
        et = Toplevel()
        et.title("PyMaster")
        et.iconbitmap('disneyland.ico')
        et.configure(bg="Pink")
        et.geometry("2000x2000")


        def sel():
            res = character.get()
            if int(res) == 1:
                global i
                global s2
                global txt
                global btn1
                global btn2
                global btn3
                global btn4
                i = 0
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
                def Run(code):
                    st = ""
                    @contextlib.contextmanager
                    def stdoutIO(stdout=None):
                        old = sys.stdout
                        if stdout is None:
                            stdout = StringIO()
                        sys.stdout = stdout
                        yield stdout
                        sys.stdout = old

                    with stdoutIO() as s:
                        try:
                            exec(code)
                        except:
                            print("Something wrong with the code")
                    st = s.getvalue()
                    global lbl
                    lbl = Label(et, text="Output : \n" + st, font=("Helvetica", 10), wraplength=500)
                    lbl.place(x=950, y=500, anchor="center")

                def Ref1():
                    s2.destroy()
                    txt.destroy()
                    btn1.destroy()
                    btn2.destroy()
                    btn3.destroy()
                    btn4.destroy()
                    btn5.destroy()

                def Ref2():
                    lbl.destroy()

                def Backtohm():
                    et.destroy()

                def Change(i):
                    Ref1()

                    if i == 0:
                        s2 = Label(et, padx=10, pady=10, text="Creating a String with single Quotes  :",
                                   font=("Helvetica", 20))
                        s2.place(x=300, y=450, anchor="center")

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

                    if i == 1:
                        s2 = Label(et, padx=10, pady=10, text="Creating a String with double Quotes  :",
                                   font=("Helvetica", 20))
                        s2.place(x=300, y=450, anchor="center")

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

                    if i == 2:
                        s2 = Label(et, padx=10, pady=10, text="Creating a String with triple Quotes  :",
                                   font=("Helvetica", 20))
                        s2.place(x=300, y=450, anchor="center")

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

                s2 = Label(et, padx=10, pady=10, text="Creating a String with single Quotes  :",
                           font=("Helvetica", 20))
                s2.place(x=300, y=450, anchor="center")

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

        labl1 = Label(et, text="Choose topic : ", padx=20, pady=20)
        labl1.configure(font=("Helvetica", 30, "bold italic"))
        labl1.place(x=200, y=100, anchor="center")


        MODES = [
            ("Strings", "1"),
        ]

        character = StringVar()
        character.set("1")
        x, y = 400, 50
        for text, mode in MODES:
            rd = Radiobutton(et, text=text, variable=character, value=mode)
            rd.configure(font=("Helvetica", 20, "bold italic"))
            rd.place(x=x, y=y)
            y += 50

        btn = Button(et, text="Select", command=sel).place(x=400, y=150)

        et.mainloop()

    else:
        response = messagebox.showwarning("Invalid!!", "Invalid Credentials")

def user():
    root2 = Tk()
    root2.title("Users")
    root2.iconbitmap("disneyland.ico")
    root2.geometry("500x500")

    # DataBases

    # Create a database or connect to one
    conn = sqlite3.connect('data_book.db')

    # Create cursor
    c = conn.cursor()

    def edit():
        # Create a database or connect to one
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        rid = del_box.get()

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

    def update():
        global ed
        ed = Tk()
        ed.title("Update Record")
        ed.iconbitmap("disneyland.ico")
        ed.geometry("500x500")

        # Create a database or connect to one
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        rid = del_box.get()
        # Insert into table
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

    def delete():
        # Create a database or connect to one
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid=" + del_box.get())
        del_box.delete(0, END)

        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()

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

    def show():
        # Create a database or connect to one
        conn = sqlite3.connect('data_book.db')

        # Create cursor
        c = conn.cursor()

        # Insert into table
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
