from tkinter import *
import mysql
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector as myconn
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

mydb = myconn.connect(host="localhost", user="root", password="", database="clinic")
mycursor = mydb.cursor()

root = tk.Tk()

root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("")

#icon
root.iconbitmap("hos.ico")

l1 = Label(root, text="").pack()
l2 = Label(root, text="Clinic Management System", font=("Helvetica 20 bold")).pack()

admin_img = Image.open('admin.png').resize((125,125))
admin_img_tk = ImageTk.PhotoImage(admin_img)

ad_img = tk.Label(root, image=admin_img_tk)
ad_img.place(x=400, y=100)

l3 = Label(root, text="ADMIN", font=("Arial 15 bold")).place(x=430,y=240)

l4 = Label(root, text="ID", font=("Arial 12")).place(x=320,y=320)
l5 = Label(root, text="Password", font=("Arial 12")).place(x=320,y=360)

id_value = IntVar()
pass_value = StringVar()

#Entry
id_entry = Entry(root, font=('helvetica 12'), textvariable=id_value).place(x=450,y=320)
pass_entry = Entry(root, font=('helvetica 12'), textvariable=pass_value).place(x=450,y=360)


def admininterface():
    global root1
    root1 = tk.Toplevel(root)  # Create Toplevel window associated with the root window
    root1.title("Admin Dashboard")
    root1.geometry("900x550+100+100")  # Position it appropriately
    root1.iconbitmap("hos.ico")

    f1 = Frame(root1, bg="royal blue", borderwidth=10)
    f1.pack(fill=X)
    l3 = Label(f1, text="Admin Dashboard", font=("helvetica 20 bold"), bg="royal blue")
    l3.pack()

    # importing images
    doc_img = Image.open('Doctor.png').resize((50, 50))
    doc_img_tk = ImageTk.PhotoImage(doc_img)

    pat_img = Image.open('Patient.png').resize((50, 50))
    pat_img_tk = ImageTk.PhotoImage(pat_img)

    dash_img = Image.open('dashboard.png').resize((50, 50))
    dash_img_tk = ImageTk.PhotoImage(dash_img)

    dash_img_label = Label(image=dash_img_tk, bg="royal blue")

    app_img = Image.open('appointment.png').resize((50, 50))
    app_img_tk = ImageTk.PhotoImage(app_img)

    # Buttons
    b1 = Button(root1, text="  Registered \n Patients  ", image=pat_img_tk, compound=LEFT, bg="pink", font=("Arial 18"), command=registered_patient)
    b1.pack(side=LEFT, padx=45)

    b2 = Button(root1, text="  Registered \n Doctors  ", image=doc_img_tk, compound=LEFT, bg="light green",
                font=("Arial 18"))
    b2.pack(side=LEFT, padx=45)

    b3 = Button(root1, text=" Appointments  ", image=app_img_tk, compound=LEFT, bg="red", font=("Arial 18"))
    b3.pack(side=LEFT, padx=45)

    root1.mainloop()

def login():
    global id_entry, pass_entry
    add_id = id_value.get()  # Changed to id_value instead of id_entry
    add_pass = pass_value.get()  # Changed to pass_value instead of pass_entry
    mycursor.execute("SELECT * FROM admin WHERE add_id = %s AND add_pass = %s", (add_id, add_pass))
    result = mycursor.fetchone()
    if result:
        # Credentials are correct, open dashboard window
        admininterface()
    else:
        # Credentials are incorrect, show error message
        messagebox.showerror("Error", "Invalid ID or password")

def registered_patient():
    root1.destroy()
    global root2
    root2 = tk.Toplevel()
    root2.geometry("1100x600")
    root2.maxsize(1100, 600)
    root2.minsize(1100, 600)
    root2.title("")

    # Icon
    root2.iconbitmap("hos.ico")

    pat_img = Image.open('pat_records.png').resize((40, 40))
    pat_img_tk = ImageTk.PhotoImage(pat_img)

    l1 = Label(root2, text="", font=('arial 18'))
    l1.pack()
    f1 = Frame(root2, bg='pink')
    f1.pack(fill=X)
    l2 = Label(f1, image=pat_img_tk, bg='pink')
    l2.pack(side=LEFT)
    l3 = Label(f1, text=" Patient Records", font=('Arial 20 bold'), bg='pink')
    l3.pack(side=LEFT)
    l4 = Label(root2, text="", font=('arial 18'))
    l4.pack()

    # Function to fetch data from MySQL and populate the treeview
    def fetch_data():
        try:
            # Execute SQL query to fetch data
            mycursor.execute("SELECT pat_name, pat_add, pat_contact FROM patient")

            # Clear existing data in the treeview
            for row in table.get_children():
                table.delete(row)

            # Insert data into the treeview
            for row in mycursor.fetchall():
                table.insert('', 'end', values=row + ("",))  # Add an empty string for the "Actions" column
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Define variables for patient details
    name_val = StringVar()
    email_val = StringVar()
    add_val = StringVar()
    con_val = StringVar(value='')  # Initialize with an empty string
    height_val = StringVar(value='')  # Initialize with an empty string
    weight_val = StringVar(value='')  # Initialize with an empty string
    blood_val = StringVar()
    id_val = StringVar()
    pass_val = StringVar()

    def add_patient():
        root2.destroy()
        global root4
        root4 = tk.Toplevel()
        root4.geometry("1100x600")
        root4.maxsize(1100, 600)
        root4.minsize(1100, 600)
        root4.title("")

        # icon
        root4.iconbitmap("hos.ico")

        def save_data():
            try:
                # Establish connection to MySQL database
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="clinic"
                )

                # Create cursor object to execute SQL queries
                mycursor = mydb.cursor()

                # Prepare SQL query to insert data into the table
                sql = "INSERT INTO patient (pat_name, pat_email, pat_contact, pat_height, pat_weight, pat_bg, pat_add, pat_id, pat_pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                name_val.get(), email_val.get(), con_val.get(), height_val.get(), weight_val.get(), blood_val.get(),
                add_val.get(), id_val.get(), pass_val.get())

                # Execute SQL query to insert data
                mycursor.execute(sql, values)

                # Commit changes to the database
                mydb.commit()

                messagebox.showinfo("Success", "Data saved successfully!")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

            finally:
                # Close the cursor and database connection
                mycursor.close()
                mydb.close()

        # Labels
        Label(root4, text="  Patient", font=("Arial 20 bold"), bg='pink').pack(side=LEFT)
        Label(root4, text="Name", font=("Arial 16")).place(x=400, y=100)
        Label(root4, text="Email", font=("Arial 16")).place(x=400, y=150)
        Label(root4, text="Contact", font=("Arial 16")).place(x=400, y=200)
        Label(root4, text="Height", font=("Arial 16")).place(x=400, y=250)
        Label(root4, text="Weight", font=("Arial 16")).place(x=400, y=300)
        Label(root4, text="Blood Group", font=("Arial 16")).place(x=400, y=350)
        Label(root4, text="Address", font=("Arial 16")).place(x=400, y=400)
        Label(root4, text="ID", font=("Arial 16")).place(x=400, y=450)
        Label(root4, text="Password", font=("Arial 16")).place(x=400, y=500)

        # Values
        name_val = StringVar()
        email_val = StringVar()
        add_val = StringVar()
        con_val = IntVar()
        height_val = IntVar()
        weight_val = IntVar()
        blood_val = StringVar()
        id_val = StringVar()
        pass_val = StringVar()

        # Entry fields
        Entry(root4, textvariable=name_val).place(x=550, y=100)
        Entry(root4, textvariable=email_val).place(x=550, y=150)
        Entry(root4, textvariable=con_val).place(x=550, y=200)
        Entry(root4, textvariable=height_val).place(x=550, y=250)
        Entry(root4, textvariable=weight_val).place(x=550, y=300)
        Entry(root4, textvariable=blood_val).place(x=550, y=350)
        Entry(root4, textvariable=add_val).place(x=550, y=400)
        Entry(root4, textvariable=id_val).place(x=550, y=450)
        Entry(root4, textvariable=pass_val).place(x=550, y=500)

        # Buttons
        Button(root4, text=" Close ", borderwidth=3, font=("Helvetica 14 bold"), command=root.quit).place(x=750, y=510)
        Button(root4, text=" Save ", borderwidth=3, font=("Helvetica 14 bold"), command=save_data).place(x=900, y=510)

        root4.mainloop()

    # Button to fetch data
    b1 = Button(f1, text="Fetch Data", font=("Arial 10 bold"), borderwidth=3, command=fetch_data)
    b1.pack(side=RIGHT)

    # Button to add a patient
    b2 = Button(f1, text="Add Patient", font=("Arial 10 bold"), borderwidth=3,
                command=add_patient)  # Add functionality as needed
    b2.pack(side=RIGHT, padx=(0, 10))

    # Create a treeview widget
    table = ttk.Treeview(root2, columns=('pat_name', 'pat_add', 'pat_contact', 'actions'), show='headings')
    table.heading('pat_name', text='Name')
    table.heading('pat_add', text='Address')
    table.heading('pat_contact', text='Contact')
    table.heading('actions', text='Actions')  # Empty column for actions
    table.pack(fill='both', expand=True)

    root2.mainloop()


#Button
b1 = Button(root, text=" Login ", font=("helvetica 13 bold"), borderwidth=2, command=login).place(x=420,y=430)


root.mainloop()