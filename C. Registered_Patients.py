from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()

root.geometry("1100x600")
root.maxsize(1100, 600)
root.minsize(1100, 600)
root.title("")

# Icon
root.iconbitmap("hos.ico")

pat_img = Image.open('pat_records.png').resize((40, 40))
pat_img_tk = ImageTk.PhotoImage(pat_img)

l1 = Label(root, text="", font=('arial 18'))
l1.pack()
f1 = Frame(root, bg='pink')
f1.pack(fill=X)
l2 = Label(f1, image=pat_img_tk, bg='pink')
l2.pack(side=LEFT)
l3 = Label(f1, text=" Patient Records", font=('Arial 20 bold'), bg='pink')
l3.pack(side=LEFT)
l4 = Label(root, text="", font=('arial 18'))
l4.pack()

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="clinic"
)

# Create cursor object to execute SQL queries
mycursor = mydb.cursor()

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

    except mysql.connector.Error as err:
        print("Error:", err)

# Define variables for patient details
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


def save_data():
    newwindow = Toplevel(root)
    newwindow.geometry("1100x600")
    newwindow.maxsize(1100, 600)
    newwindow.minsize(1100, 600)
    newwindow.title("Add Patient")

    # Labels
    Label(newwindow, text="  Patient", font=("Arial 20 bold"), bg='pink').pack(side=LEFT)
    Label(newwindow, text="Name", font=("Arial 16")).place(x=400, y=100)
    Label(newwindow, text="Email", font=("Arial 16")).place(x=400, y=150)
    Label(newwindow, text="Contact", font=("Arial 16")).place(x=400, y=200)
    Label(newwindow, text="Height", font=("Arial 16")).place(x=400, y=250)
    Label(newwindow, text="Weight", font=("Arial 16")).place(x=400, y=300)
    Label(newwindow, text="Blood Group", font=("Arial 16")).place(x=400, y=350)
    Label(newwindow, text="Address", font=("Arial 16")).place(x=400, y=400)
    Label(newwindow, text="ID", font=("Arial 16")).place(x=400, y=450)
    Label(newwindow, text="Password", font=("Arial 16")).place(x=400, y=500)

    # Entry fields
    Entry(newwindow, textvariable=name_val).place(x=550, y=100)
    Entry(newwindow, textvariable=email_val).place(x=550, y=150)
    Entry(newwindow, textvariable=con_val).place(x=550, y=200)
    Entry(newwindow, textvariable=height_val).place(x=550, y=250)
    Entry(newwindow, textvariable=weight_val).place(x=550, y=300)
    Entry(newwindow, textvariable=blood_val).place(x=550, y=350)
    Entry(newwindow, textvariable=add_val).place(x=550, y=400)
    Entry(newwindow, textvariable=id_val).place(x=550, y=450)
    Entry(newwindow, textvariable=pass_val).place(x=550, y=500)

    # Buttons
    Button(newwindow, text=" Close ", borderwidth=3, font=("Helvetica 14 bold"), command=newwindow.destroy).place(x=750, y=510)
    Button(newwindow, text=" Save ", borderwidth=3, font=("Helvetica 14 bold"), command=save_patient_data).place(x=900, y=510)

    newwindow.mainloop()
def save_patient_data():
    # This function will be called when the "Save" button is clicked
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
        values = (name_val.get(), email_val.get(), con_val.get(), height_val.get(), weight_val.get(), blood_val.get(), add_val.get(), id_val.get(), pass_val.get())

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

# Button to fetch data
b1 = Button(f1, text="Fetch Data", font=("Arial 10 bold"), borderwidth=3, command=fetch_data)
b1.pack(side=RIGHT)

# Button to add a patient
b2 = Button(f1, text="Add Patient", font=("Arial 10 bold"), borderwidth=3, command=save_data)  # Add functionality as needed
b2.pack(side=RIGHT, padx=(0, 10))

# Create a treeview widget
table = ttk.Treeview(root, columns=('pat_name', 'pat_add', 'pat_contact', 'actions'), show='headings')
table.heading('pat_name', text='Name')
table.heading('pat_add', text='Address')
table.heading('pat_contact', text='Contact')
table.heading('actions', text='Actions')  # Empty column for actions
table.pack(fill='both', expand=True)

root.mainloop()
