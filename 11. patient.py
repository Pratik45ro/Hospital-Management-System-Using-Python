from datetime import datetime
from tkinter import *

import mysql
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector as myconn
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

root = tk.Tk()
root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("")

#icon
root.iconbitmap("hos.ico")

l1 = Label(root, text="").pack()
l2 = Label(root, text="Clinic Management System", font=("Helvetica 20 bold")).pack()

pat_img = Image.open('patient.png').resize((125,125))
pat_img_tk = ImageTk.PhotoImage(pat_img)

ad_img = tk.Label(root, image=pat_img_tk)
ad_img.place(x=400, y=100)

l3 = Label(root, text="PATIENT", font=("Arial 15 bold")).place(x=420,y=240)

l4 = Label(root, text="ID", font=("Arial 12")).place(x=320,y=320)
l5 = Label(root, text="Password", font=("Arial 12")).place(x=320,y=360)

id_value = IntVar()
pass_value = StringVar()

#Entry
id_entry = (Entry(root, font=('helvetica 12'), textvariable=id_value))
id_entry.place(x=450,y=320)
pass_entry = (Entry(root, font=('helvetica 12'), textvariable=pass_value, show='*'))
pass_entry.place(x=450,y=360)

# Define global variables for entry fields
name_val = StringVar()
email_val = StringVar()
con_val = StringVar()
height_val = IntVar()
weight_val = IntVar()
blood_val = StringVar()
add_val = StringVar()
dob_val = IntVar()

def Navigate():
    global name_val, email_val, con_val, height_val, weight_val, blood_val, add_val, dob_val
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

        # Retrieve patient ID and password from entry widgets
        pat_id = id_entry.get()
        pat_pass = pass_entry.get()

        # Execute SQL query to check credentials and fetch patient details
        mycursor.execute("SELECT * FROM patient WHERE pat_id = %s AND pat_pass = %s", (pat_id, pat_pass))

        # Fetch the result
        result = mycursor.fetchone()

        # Close the cursor and database connection
        mycursor.close()
        mydb.close()

        # Check if the result is not None (i.e., if credentials are correct)
        if result:
            # Populate entry fields with fetched patient details
            id_value.set(result[0])
            name_val.set(result[1])  # Correct the index here
            email_val.set(result[3])  # Adjust indices according to your database schema
            con_val.set(result[4])
            height_val.set(result[5])
            weight_val.set(result[6])
            blood_val.set(result[7])
            add_val.set(result[8])
            dob_val.set(result[9])
            # Open patient dashboard window
            Patient_dashboard()
        else:
            # Credentials are incorrect, show error message
            messagebox.showerror("Error", "Invalid ID or password")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"MySQL Error: {err}")

def Patient_dashboard():
    global root5
    root5 = tk.Toplevel()
    root5 = Toplevel(root)
    root5.geometry("900x550")
    root5.maxsize(900, 550)
    root5.minsize(900, 550)
    root5.title("")

    # icon
    root5.iconbitmap("hos.ico")

    l0 = Label(root5, text="", font=("arial 16")).pack()
    f1 = Frame(root5, bg='lavender')
    f1.pack(fill=X)
    l1 = Label(f1, text=" Profile", font=("Arial 20 bold"), fg='purple', bg='lavender')
    l1.pack(side=LEFT)

    def BookApp():
        global root6
        root6 = tk.Toplevel(root5)  # Create a Toplevel window as a child of root5

        def fetch_patient_data():
            try:
                # Establish connection to MySQL database
                mydb = myconn.connect(
                    host="localhost",
                    user="root",  # Replace with your MySQL username
                    passwd="",  # Replace with your MySQL password
                    database="clinic"  # Replace with your MySQL database name
                )

                # Create cursor object to execute SQL queries
                mycursor = mydb.cursor()

                # Execute SQL query to fetch data from the patient table
                mycursor.execute("SELECT name, ID FROM patient")

                # Fetch all rows
                patient_data = mycursor.fetchall()

                # Close cursor and database connection
                mycursor.close()
                mydb.close()

                return patient_data

            except myconn.Error as e:
                print("Error:", e)
                return None

        def populate_patient_data():
            patient_data = fetch_patient_data()
            if patient_data:
                for name, ID in patient_data:
                    # Process the fetched data as needed
                    print("Name:", name, "ID:", ID)
                    # You can further populate your GUI with this data
                    # For demonstration, I'm just printing the data

        def update_date(date_label=None):
            current_date = datetime.now().strftime("%Y-%m-%d")
            date_label.config(text=current_date)
            root6.after(1000, update_date)

        def populate_table():
            try:
                # Establish connection to MySQL database
                mydb = myconn.connect(
                    host="localhost",
                    user="root",  # Replace with your MySQL username
                    passwd="",  # Replace with your MySQL password
                    database="clinic"  # Replace with your MySQL database name
                )

                # Create cursor object to execute SQL queries
                mycursor = mydb.cursor()

                # Execute SQL query to retrieve data for specific columns
                mycursor.execute(
                    "SELECT doctor_name, doctor_specialist, doctor_experience, doctor_timing FROM appointment")

                # Fetch all rows
                rows = mycursor.fetchall()

                # Populate the Treeview with fetched data
                for row in rows:
                    table.insert('', 'end', values=row)

                # Commit changes and close cursor
                mydb.commit()
                mycursor.close()

            except myconn.Error as e:
                print("Error:", e)

        def book_appointment():
            try:
                # Get the selected item from the Treeview
                selected_item = table.selection()[0]
                values = table.item(selected_item, 'values')

                # Establish connection to MySQL database
                mydb = myconn.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="clinic"
                )

                # Create cursor object to execute SQL queries
                mycursor = mydb.cursor()

                # Insert appointment details into the pat_history table
                Dr_name = values[0]
                date = date_label.cget("text")
                time = values[3]

                # Sample SQL query to insert appointment data into the pat_history table
                sql = "INSERT INTO pat_history (Dr_name, date, time) VALUES (%s, %s, %s)"
                values = (Dr_name, date, time)
                mycursor.execute(sql, values)

                # Commit changes
                mydb.commit()

                # Close cursor and database connection
                mycursor.close()
                mydb.close()

                # Show success messagebox
                messagebox.showinfo("Success", "Appointment booked successfully!")

            except Exception as e:
                print("Error:", e)

        # Define root6 window properties
        root6.geometry("1100x600")
        root6.maxsize(1100, 600)
        root6.minsize(1100, 600)
        root6.title("")
        root6.iconbitmap("hos.ico")

        # Create and pack widgets
        l1 = Label(root6, text='', font=('arial 14'))
        l1.pack()
        f1 = Frame(root6, bg='orange')
        f1.pack(fill=X)
        l2 = Label(f1, text="Appointment Booking", font=('arial 20 bold'), bg='orange')
        l2.pack()
        l3 = Label(root6, text='', font=('arial 14'))
        l3.pack()

        pat_img = Image.open('patient.png').resize((100, 100))
        pat_img_tk = ImageTk.PhotoImage(pat_img)

        pat_img_label = Label(root6, image=pat_img_tk)
        pat_img_label.place(x=30, y=120)

        l4 = Label(root6, text="Name", font=('helvetica 15 bold'))
        l4.pack(pady=5)
        e1 = Entry(root6)
        e1.place(x=600, y=100)
        l5 = Label(root6, text="ID", font=('helvetica 15 bold'))
        l5.pack(pady=5)
        e2 = Entry(root6)
        e2.place(x=600, y=140)

        l6 = Label(root6, text="Date of Appointment", font=('helvetica 15'))
        l6.pack(pady=5)
        date_label = Label(root6, font=('helvetica 15'))
        date_label.pack()
        update_date(date_label)  # Call update_date to start updating date

        l7 = Label(root6, text='', font=('arial 14'))
        l7.pack()

        table = ttk.Treeview(root6, columns=('1', '2', '3', '4'), show='headings')
        table.heading('1', text='Doctor name')
        table.heading('2', text='Specialist')
        table.heading('3', text='Experience')
        table.heading('4', text='Timing')
        table.pack(fill='both', expand=True)

        # Populate the Treeview with data
        populate_table()

        # Button to book an appointment
        book_button = Button(root6, text="Book", font=('arial 11 bold'), command=book_appointment)
        book_button.pack(padx=30, pady=10)

        # Call the function to populate patient data when the GUI is initialized
        populate_patient_data()

        root6.mainloop()

    def Pat_History():
        global root7
        root7 = tk.Toplevel()
        root7.geometry("900x550")
        root7.maxsize(900, 550)
        root7.minsize(900, 550)
        root7.title("")

        # Icon
        root7.iconbitmap("hos.ico")

        l1 = Label(root7, text='', font=('arial 14'))
        l1.pack()
        f1 = Frame(root7, bg='orange')
        f1.pack(fill=X)
        l2 = Label(f1, text=" Patient History", font=('arial 20 bold'), bg='orange')
        l2.pack()
        l3 = Label(root7, text='', font=('arial 14'))
        l3.pack()

        pat_img = Image.open('patient.png').resize((100, 100))
        pat_img_tk = ImageTk.PhotoImage(pat_img)

        pat_img_label = Label(root7, image=pat_img_tk)
        pat_img_label.place(x=30, y=120)

        l4 = Label(root7, text="Name", font=('helvetica 15 bold'))
        l4.pack(pady=10)
        name_val = StringVar()  # Variable to store the name
        e1 = Entry(root7, textvariable=name_val)
        e1.place(x=500, y=100)
        l5 = Label(root7, text="ID", font=('helvetica 15 bold'))
        l5.pack(pady=10)
        id_val = StringVar()  # Variable to store the ID
        e2 = Entry(root7, textvariable=id_val)
        e2.place(x=500, y=160)

        l6 = Label(root7, text='', font=('arial 14'))
        l6.pack()
        l7 = Label(root7, text='', font=('arial 14'))
        l7.pack()
        f2 = Frame(root7, bg='red')
        f2.pack(fill=X)
        l8 = Label(f2, text=" Appointments", font=('helvetica 18 bold'), bg='red')
        l8.pack(side=LEFT)

        table = ttk.Treeview(root7, columns=('first', 'second', 'third', 'fourth'), show='headings')
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
        fetch_data_button = Button(root7, text="Fetch Patient Data", font=('Helvetica 12 bold'),
                                   command=fetch_patient_data)
        fetch_data_button.place(x=300, y=200)

        root7.mainloop()

    b1 = Button(f1, text="Book Appointment", font=('Helvetica 13 bold'), fg='red', bg='lavender', borderwidth=2, command=BookApp)
    b1.pack(side=RIGHT, padx=10)
    b2 = Button(f1, text="History", font=('Helvetica 13 bold'), fg='black', bg='lavender', borderwidth=2, command=Pat_History)
    b2.pack(side=RIGHT, padx=10)

    # patient icon
    pat_img = Image.open('patient.png').resize((100, 100))
    pat_img_tk = ImageTk.PhotoImage(pat_img)
    ad_img = tk.Label(root5, image=pat_img_tk)
    ad_img.place(x=40, y=80)

    # Labels and Entry fields
    fields = [
        ("Name:", name_val),
        ("ID:", id_value),
        ("Email:", email_val),
        ("Contact:", con_val),
        ("Height:", height_val),
        ("Weight:", weight_val),
        ("BG:", blood_val),
        ("Address:", add_val),
        ("D.O.B:", dob_val)
    ]

    y_position = 120  # Initial Y position for labels and entry fields

    for label_text, variable in fields:
        label = Label(root5, text=label_text, font=("Arial 16"))
        label.place(x=350, y=y_position)

        entry = Entry(root5, textvariable=variable)
        entry.place(x=450, y=y_position + 5)

        y_position += 40  # Increment Y position for the next label and entry field

    root5.mainloop()


#Button
b1 = Button(root, text=" Login ", font=("helvetica 13 bold"), borderwidth=2, command=Navigate).place(x=420,y=430)

root.mainloop()
