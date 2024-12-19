from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import mysql.connector

root = Tk()

root.geometry("900x550")
root.maxsize(900, 550)
root.minsize(900, 550)
root.title("")

# Icon
root.iconbitmap("hos.ico")

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
        mycursor.execute("SELECT pat_name, pat_dob, pat_contact, pat_email FROM patient")  # Modify the query as per your database schema

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
l1 = Label(root, text="", font=('Arial 18'))
l1.pack()
f1 = Frame(root, bg='pink')
f1.pack(fill=X)
l2 = Label(f1, text="   Patient Details", font=('Arial 20 bold'), bg='pink')
l2.pack(side=LEFT)
l3 = Label(root, text="", font=('Arial 18'))
l3.pack()

# Treeview Widget
table = ttk.Treeview(root, columns=('first', 'second', 'third', 'fourth'), show='headings')
table.heading('first', text='Name')
table.heading('second', text='Date of Birth')
table.heading('third', text='Contact')
table.heading('fourth', text='Email')
table.pack(fill='both', expand=True)

# Populate the Treeview initially
populate_table()

root.mainloop()
