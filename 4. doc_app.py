from tkinter import *

import mysql
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user="root", password="", database="clinic")
mycursor = mydb.cursor()

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
        mycursor.execute("SELECT pat_name, pat_id FROM patient")  # Modify the query as per your database schema

        # Fetch all rows
        rows = mycursor.fetchall()

        # Clear existing data in the Treeview
        for item in table.get_children():
            table.delete(item)

        # Populate the Treeview with fetched data
        for row in rows:
            table.insert('', 'end', values=row + ('Prescribe',))  # Add 'Prescribe' to each row

        # Commit changes and close cursor
        mydb.commit()
        mycursor.close()

    except mysql.connector.Error as e:
        print("Error:", e)

# Labels and Entry
l1 = Label(root, text="", font=('arial 14'))
l1.pack()
f1 = Frame(root, bg='red')
f1.pack(fill=X)
l2 = Label(f1, text=" Appointments", font=('Arial 18 bold'), bg='red')
l2.pack(side=LEFT)

f2 = Frame(root)
f2.pack(fill=X)

date_val = IntVar()

e1 = Entry(f2, textvariable=date_val)
e1.pack(side=RIGHT)

l3 = Label(f2, text="Date:  ", font=('helvetica 15'))
l3.pack(side=RIGHT)

l4 = Label(root, text="", font=('arial 14'))
l4.pack()

# Treeview Widget
table = ttk.Treeview(root, columns=('1', '2'), show='headings')  # Remove the '3' column
table.heading('1', text='Name')
table.heading('2', text='ID')
table.pack(fill=BOTH, expand=True)

# Populate the Treeview initially
populate_table()

def prescribe_selected():
    global root14
    root14 = tk.Toplevel()
    root14.iconbitmap("hos.ico")

    l1 = Label(root14, text="", font=('arial 14'))
    l1.pack()
    l2 = Label(root14, text="", font=('arial 14'))
    l2.pack()

    root14.geometry("900x550")
    root14.maxsize(900, 550)
    root14.minsize(900, 550)

    f1 = Frame(root14)
    f1.pack(fill=X)

    patient_image = Image.open("patient.png").resize((100, 100))
    patient_image_tk = ImageTk.PhotoImage(patient_image)

    image_label = tk.Label(f1, image=patient_image_tk)
    image_label.pack(side=LEFT, padx=30, pady=10)

    # Entry Values
    name_val = StringVar()
    age_val = IntVar()
    id_val = IntVar()
    height_val = IntVar()
    weight_val = IntVar()
    blood_val = StringVar()

    # Function to fetch patient data and pre-fill entry fields
    def fetch_patient_data():
        try:
            patient_id = id_val.get()
            mycursor.execute("SELECT * FROM patient WHERE pat_id = %s", (patient_id,))
            patient_data = mycursor.fetchone()
            if patient_data:
                name_val.set(patient_data[1])
                age_val.set(patient_data[2])
                height_val.set(patient_data[3])
                weight_val.set(patient_data[4])
                blood_val.set(patient_data[5])
                messagebox.showinfo("Success", "Patient data fetched successfully.")
            else:
                messagebox.showerror("Error", "Patient with the specified ID not found.")
        except Exception as e:
            print("Error fetching patient data:", e)

    # Labels and Entry
    l1 = Label(root14, text='Name', font=('helvetica 13'))
    l1.place(x=200, y=50)
    e1 = Entry(root14, textvariable=name_val)
    e1.place(x=300, y=50)

    l2 = Label(root14, text='Id', font=('helvetica 13'))
    l2.place(x=200, y=100)
    e2 = Entry(root14, textvariable=id_val)
    e2.place(x=300, y=100)

    l3 = Label(root14, text='Age', font=('helvetica 13'))
    l3.place(x=200, y=150)
    e3 = Entry(root14, textvariable=age_val)
    e3.place(x=300, y=150)

    l4 = Label(root14, text='Height', font=('helvetica 13'))
    l4.place(x=520, y=50)
    e4 = Entry(root14, textvariable=height_val)
    e4.place(x=650, y=50)

    l5 = Label(root14, text='Weight', font=('helvetica 13'))
    l5.place(x=520, y=100)
    e5 = Entry(root14, textvariable=weight_val)
    e5.place(x=650, y=100)

    l6 = Label(root14, text='Blood Group', font=('helvetica 13'))
    l6.place(x=520, y=150)
    e6 = Entry(root14, textvariable=blood_val)
    e6.place(x=650, y=150)

    l7 = Label(root14, text="", font=('arial 14'))
    l7.pack()

    l8 = Label(root14, text="", font=('arial 14'))
    l8.pack()

    f2 = Frame(root14, bg='light green')
    f2.pack(fill=X)

    l9 = Label(f2, text='Prescription', font=('helvetica 15 bold'), bg='light green')
    l9.pack()

    entry = Text(root14)
    entry.place(x=10, y=280, width=880, height=150)

    # Function to prescribe
    def prescribe():
        # Get prescription text from entry widget
        prescription_text = entry.get("1.0", "end-1c")
        # Insert prescription into the database
        try:
            sql = "INSERT INTO prescription (prescription_details) VALUES (%s)"
            val = (prescription_text,)  # Note the comma to create a tuple
            mycursor.execute(sql, val)
            mydb.commit()
            print("Prescription saved successfully.")

            # Update the prescription column for the patient in pat_history table
            patient_name = name_val.get()
            doctor_name = "Binod"  # Update this with the actual doctor's name
            update_sql = "UPDATE pat_history SET prescription = %s WHERE dr_name = %s"
            update_val = (prescription_text, doctor_name)
            mycursor.execute(update_sql, update_val)
            mydb.commit()
            print("Prescription updated in pat_history table.")

            # Show success messagebox
            messagebox.showinfo("Success", "Prescription saved successfully.")
        except Exception as e:
            print("Error saving prescription:", e)

    # Button to prescribe
    prescribe_button = Button(root14, text="Submit", font=('Helvetica 12 bold'), command=prescribe)
    prescribe_button.place(x=400, y=450)

    # Button to fetch patient data
    fetch_data_button = Button(root14, text="Fetch Patient Data", font=('Helvetica 12 bold'), command=fetch_patient_data)
    fetch_data_button.place(x=250, y=450)

    root14.mainloop()


# Button to prescribe
prescribe_button = Button(root, text="Prescribe", command=prescribe_selected)
prescribe_button.pack()

root.mainloop()
