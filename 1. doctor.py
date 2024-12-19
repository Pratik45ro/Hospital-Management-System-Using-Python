from tkinter import *

import mysql
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector as myconn
from tkinter import messagebox, ttk


def doctor_dashboard():
    global root8
    root8 = tk.Toplevel()
    root8.geometry("900x550")
    root8.maxsize(900, 550)
    root8.minsize(900, 550)
    root8.title("")

    # icon
    root8.iconbitmap("hos.ico")

    l1 = Label(root8, text="")
    l1.pack()
    l2 = Label(root8, text="")
    l2.pack()
    f1 = Frame(root8, bg="royal blue", borderwidth=10)
    f1.pack(fill=X)
    l3 = Label(f1, text="Dashboard", font=("helventica 20 bold"), bg="royal blue")
    l3.pack()

    dash_img = Image.open('dashboard.png').resize((50, 50))
    dash_img_tk = ImageTk.PhotoImage(dash_img)

    pat_img = Image.open("tpatients.png").resize((50, 50))
    pat_img_tk = ImageTk.PhotoImage(pat_img)

    app_img = Image.open('appointment.png').resize((50, 50))
    app_img_tk = ImageTk.PhotoImage(app_img)

    dash_img_label = Label(image=dash_img_tk, bg="royal blue")
    dash_img_label.place(x=310, y=44)

    def pat_details():
        global root9
        root9 = tk.Toplevel()
        root9.geometry("900x550")
        root9.maxsize(900, 550)
        root9.minsize(900, 550)
        root9.title("")

        # Icon
        root9.iconbitmap("hos.ico")

        # Function to fetch data from MySQL and populate the Treeview
        def populate_table():
            try:
                # Establish connection to MySQL database
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Replace with your MySQL username
                    passwd="",  # Replace with your MySQL password
                    database="clinic"  # Replace with your MySQL database name
                )

                # Create cursor object to execute SQL queries
                mycursor = mydb.cursor()

                # Execute SQL query to retrieve data
                mycursor.execute(
                    "SELECT pat_name, pat_dob, pat_contact, pat_email FROM patient")  # Modify the query as per your database schema

                # Fetch all rows
                rows = mycursor.fetchall()

                # Clear existing data in the Treeview
                for item in table.get_children():
                    table.delete(item)

                # Populate the Treeview with fetched data
                for row in rows:
                    table.insert('', 'end', values=row)

                # Commit changes and close cursor
                mydb.commit()
                mycursor.close()

            except mysql.connector.Error as e:
                print("Error:", e)

        # Labels and Entries
        l1 = Label(root9, text="", font=('Arial 18'))
        l1.pack()
        f1 = Frame(root9, bg='pink')
        f1.pack(fill=X)
        l2 = Label(f1, text="   Patient Details", font=('Arial 20 bold'), bg='pink')
        l2.pack(side=LEFT)
        l3 = Label(root9, text="", font=('Arial 18'))
        l3.pack()

        # Treeview Widget
        table = ttk.Treeview(root9, columns=('first', 'second', 'third', 'fourth'), show='headings')
        table.heading('first', text='Name')
        table.heading('second', text='Date of Birth')
        table.heading('third', text='Contact')
        table.heading('fourth', text='Email')
        table.pack(fill='both', expand=True)

        # Populate the Treeview initially
        populate_table()

        root9.mainloop()

    def Doc_app():
        global root10
        root10 = tk.Toplevel()
        root10.geometry("900x550")
        root10.maxsize(900, 550)
        root10.minsize(900, 550)
        root10.title("")

        # Icon
        root10.iconbitmap("hos.ico")

        # Function to fetch data from MySQL and populate the Treeview
        def populate_table():
            try:
                # Establish connection to MySQL database
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Replace with your MySQL username
                    passwd="",  # Replace with your MySQL password
                    database="clinic"  # Replace with your MySQL database name
                )

                # Create cursor object to execute SQL queries
                mycursor = mydb.cursor()

                # Execute SQL query to retrieve data
                mycursor.execute("SELECT pat_name, pat_id FROM patient")  # Modify the query as per your database schema

                # Fetch all rows
                rows = mycursor.fetchall()

                # Clear existing data in the Treeview
                for item in table.get_children():
                    table.delete(item)

                # Populate the Treeview with fetched data
                for row in rows:
                    table.insert('', 'end', values=row)

                # Commit changes and close cursor
                mydb.commit()
                mycursor.close()

            except mysql.connector.Error as e:
                print("Error:", e)

        # Labels and Entry
        l1 = Label(root10, text="", font=('arial 14'))
        l1.pack()
        f1 = Frame(root10, bg='red')
        f1.pack(fill=X)
        l2 = Label(f1, text=" Appointments", font=('Arial 18 bold'), bg='red')
        l2.pack(side=LEFT)

        f2 = Frame(root10)
        f2.pack(fill=X)

        date_val = IntVar()

        e1 = Entry(f2, textvariable=date_val)
        e1.pack(side=RIGHT)

        l3 = Label(f2, text="Date:  ", font=('helvetica 15'))
        l3.pack(side=RIGHT)

        l4 = Label(root10, text="", font=('arial 14'))
        l4.pack()

        # Treeview Widget
        table = ttk.Treeview(root10, columns=('1', '2', '3'), show='headings')
        table.heading('1', text='Name')
        table.heading('2', text='ID')
        table.heading('3', text='Action')
        table.pack(fill=BOTH, expand=True)

        # Populate the Treeview initially
        populate_table()

        root10.mainloop()

    # Buttons
    b1 = Button(root8, text=" Total Patients ", image=pat_img_tk, compound=LEFT, bg='pink', font=("Arial 18"),
                borderwidth=2, command=pat_details)
    b1.pack(side=LEFT, padx=60)

    b2 = Button(root8, text=" Appointments ", image=app_img_tk, compound=LEFT, bg='red', font=("Arial 18"),
                borderwidth=2, command=Doc_app)
    b2.pack(side=LEFT, padx=60)

    root8.mainloop()

# Define the login function first
def login():
    global id_entry, pass_entry, mycursor
    add_id = id_entry.get()
    add_pass = pass_entry.get()
    mycursor.execute("SELECT * FROM doctor WHERE doc_id = %s AND doc_pass = %s", (add_id, add_pass))
    result = mycursor.fetchone()
    if result:
        # Credentials are correct, open dashboard window
        doctor_dashboard()
    else:
        # Credentials are incorrect, show error message
        messagebox.showerror("Error", "Invalid ID or password")

# Connect to MySQL
mydb = myconn.connect(host="localhost", user="root", password="", database="clinic")
mycursor = mydb.cursor()

root = Tk()

root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("")

#icon
root.iconbitmap("hos.ico")

l1 = Label(root, text="").pack()
l2 = Label(root, text="Hospital Management System", font=("Helvetica 20 bold")).pack()

doc_img = Image.open('doctor.png').resize((125,125))
doc_img_tk = ImageTk.PhotoImage(doc_img)

ad_img = tk.Label(root, image=doc_img_tk)
ad_img.place(x=400, y=100)

l3 = Label(root, text="DOCTOR", font=("Arial 15 bold")).place(x=420,y=240)

l4 = Label(root, text="ID", font=("Arial 12")).place(x=320,y=320)
l5 = Label(root, text="Password", font=("Arial 12")).place(x=320,y=360)

id_value = IntVar()
pass_value = StringVar()

#Entry
id_entry = Entry(root, font=('helvetica 12'), textvariable=id_value)
id_entry.place(x=450,y=320)
pass_entry = Entry(root, font=('helvetica 12'), textvariable=pass_value, show='*')
pass_entry.place(x=450,y=360)

#Button
b1 = Button(root, text=" Login ", font=("helvetica 13 bold"), borderwidth=2, command=login)
b1.place(x=420,y=430)

root.mainloop()
