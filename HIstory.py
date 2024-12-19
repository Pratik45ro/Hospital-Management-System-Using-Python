from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()

root.geometry("900x550")
root.maxsize(900, 550)
root.minsize(900, 550)
root.title("")

# Icon
root.iconbitmap("hos.ico")

l1 = Label(root, text='', font=('arial 14'))
l1.pack()
f1 = Frame(root, bg='orange')
f1.pack(fill=X)
l2 = Label(f1, text=" Patient History", font=('arial 20 bold'), bg='orange')
l2.pack()
l3 = Label(root, text='', font=('arial 14'))
l3.pack()

pat_img = Image.open('patient.png').resize((100, 100))
pat_img_tk = ImageTk.PhotoImage(pat_img)

pat_img_label = Label(root, image=pat_img_tk)
pat_img_label.place(x=30, y=120)

l4 = Label(root, text="Name", font=('helvetica 15 bold'))
l4.pack(pady=10)
name_val = StringVar()  # Variable to store the name
e1 = Entry(root, textvariable=name_val)
e1.place(x=500, y=100)
l5 = Label(root, text="ID", font=('helvetica 15 bold'))
l5.pack(pady=10)
id_val = StringVar()  # Variable to store the ID
e2 = Entry(root, textvariable=id_val)
e2.place(x=500, y=160)

l6 = Label(root, text='', font=('arial 14'))
l6.pack()
l7 = Label(root, text='', font=('arial 14'))
l7.pack()
f2 = Frame(root, bg='red')
f2.pack(fill=X)
l8 = Label(f2, text=" Appointments", font=('helvetica 18 bold'), bg='red')
l8.pack(side=LEFT)

table = ttk.Treeview(root, columns=('first', 'second', 'third', 'fourth'), show='headings')
table.heading('first', text='Date')
table.heading('second', text='Doctor Name')
table.heading('third', text='Time')
table.heading('fourth', text='Prescription')  # Added Prescription column
table.pack(fill='both', expand=True)


# Function to populate the Treeview with data from MySQL pat_history table
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

        # Execute SQL query to retrieve data from pat_history table
        mycursor.execute("SELECT date, Dr_name, time, prescription FROM pat_history")

        # Fetch all rows
        rows = mycursor.fetchall()

        # Populate the Treeview with fetched data
        for row in rows:
            table.insert('', 'end', values=row)

        # Commit changes and close cursor
        mydb.commit()
        mycursor.close()

    except mysql.connector.Error as e:
        print("Error:", e)


# Function to fetch patient data from the patient table based on the provided patient ID
def fetch_patient_data():
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

        # Get the patient ID from the Entry field
        patient_id = e2.get()

        # Execute SQL query to retrieve patient data based on ID
        mycursor.execute("SELECT pat_name FROM patient WHERE pat_id = %s", (patient_id,))

        # Fetch the row
        row = mycursor.fetchone()

        if row:
            # Set the Name Entry field with the fetched patient name
            name_val.set(row[0])
            # Set the ID Entry field with the fetched patient ID
            id_val.set(patient_id)
        else:
            # If no patient found with the specified ID, clear the Name and ID Entry fields
            name_val.set('')
            id_val.set('')
            messagebox.showerror("Error", "Patient with the specified ID not found.")

        # Commit changes and close cursor
        mydb.commit()
        mycursor.close()

    except mysql.connector.Error as e:
        print("Error:", e)


# Populate the Treeview with data
populate_table()

# Button to fetch patient data
fetch_data_button = Button(root, text="Fetch Patient Data", font=('Helvetica 12 bold'), command=fetch_patient_data)
fetch_data_button.place(x=300, y=200)

root.mainloop()
