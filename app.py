from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

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

        # Execute SQL query to fetch data from the patient table
        mycursor.execute("SELECT name, ID FROM patient")

        # Fetch all rows
        patient_data = mycursor.fetchall()

        # Close cursor and database connection
        mycursor.close()
        mydb.close()

        return patient_data

    except mysql.connector.Error as e:
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
    root.after(1000, update_date)

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

        # Execute SQL query to retrieve data for specific columns
        mycursor.execute("SELECT doctor_name, doctor_specialist, doctor_experience, doctor_timing FROM appointment")

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

def book_appointment():
    try:
        # Get the selected item from the Treeview
        selected_item = table.selection()[0]
        values = table.item(selected_item, 'values')

        # Establish connection to MySQL database
        mydb = mysql.connector.connect(
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

root = Tk()
root.geometry("1100x600")
root.maxsize(1100, 600)
root.minsize(1100, 600)
root.title("")
root.iconbitmap("hos.ico")

l1 = Label(root, text='', font=('arial 14'))
l1.pack()
f1 = Frame(root, bg='orange')
f1.pack(fill=X)
l2 = Label(f1, text="Appointment Booking", font=('arial 20 bold'), bg='orange')
l2.pack()
l3 = Label(root, text='', font=('arial 14'))
l3.pack()

pat_img = Image.open('patient.png').resize((100, 100))
pat_img_tk = ImageTk.PhotoImage(pat_img)

pat_img_label = Label(root, image=pat_img_tk)
pat_img_label.place(x=30, y=120)

l4 = Label(root, text="Name", font=('helvetica 15 bold'))
l4.pack(pady=5)
e1 = Entry(root)
e1.place(x=600, y=100)
l5 = Label(root, text="ID", font=('helvetica 15 bold'))
l5.pack(pady=5)
e2 = Entry(root)
e2.place(x=600, y=140)

l6 = Label(root, text="Date of Appointment", font=('helvetica 15'))
l6.pack(pady=5)
date_label = Label(root, font=('helvetica 15'))
date_label.pack()
update_date(date_label)  # Call update_date to start updating date

l7 = Label(root, text='', font=('arial 14'))
l7.pack()

table = ttk.Treeview(root, columns=('1', '2', '3', '4'), show='headings')
table.heading('1', text='Doctor name')
table.heading('2', text='Specialist')
table.heading('3', text='Experience')
table.heading('4', text='Timing')
table.pack(fill='both', expand=True)

# Populate the Treeview with data
populate_table()

# Button to book an appointment
book_button = Button(root, text="Book", font=('arial 11 bold'), command=book_appointment)
book_button.pack(padx=30, pady=10)

# Call the function to populate patient data when the GUI is initialized
populate_patient_data()

root.mainloop()
