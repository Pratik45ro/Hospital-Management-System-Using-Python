from tkinter import *
import datetime
import mysql
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import mysql.connector as myconn
from tkinter import messagebox
import customtkinter as ctk

mydb = myconn.connect(host="localhost", user="root", password="", database="clinic")
mycursor = mydb.cursor()

root = Tk()

root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("")

#icon
root.iconbitmap("hos.ico")


f1 = Frame(root, bg="Orange", borderwidth=8, )
f1.pack(side=LEFT, fill="y")

la1 = Label(f1, text="Login As", font=("TimesNewRoman 12 bold"), bg="Orange").pack(pady=225)

l = Label(root, text="").pack()
l1 = Label(root, text="").pack()
l2 = Label(root, text="").pack()
l3 = Label(root, text="Clinic Management System", font=("Arial 25 bold")).pack()
l4 = Label(root, text="").pack()

#importing images
doc_img = Image.open('Doctor.png').resize((120,120))
doc_img_tk = ImageTk.PhotoImage(doc_img)

pat_img = Image.open('Patient.png').resize((120,120))
pat_img_tk = ImageTk.PhotoImage(pat_img)

admin_img = Image.open('Admin.png').resize((120,120))
admin_img_img_tk = ImageTk.PhotoImage(admin_img)


def is_valid_contact(contact):
    # Check if contact is a 10-digit number
    return len(contact) == 10 and contact.isdigit()
def Leaf(): #AdminLogin
    global adminlogin
    adminlogin = tk.Toplevel()
    adminlogin.geometry("900x550")
    adminlogin.maxsize(900, 550)
    adminlogin.minsize(900, 550)
    adminlogin.title("")

    # icon
    adminlogin.iconbitmap("hos.ico")

    l1 = Label(adminlogin, text="").pack()
    l2 = Label(adminlogin, text="Clinic Management System", font=("Helvetica 20 bold")).pack()

    admin_img = Image.open('admin.png').resize((125, 125))
    admin_img_tk = ImageTk.PhotoImage(admin_img)

    ad_img = tk.Label(adminlogin, image=admin_img_tk)
    ad_img.place(x=400, y=100)

    l3 = Label(adminlogin, text="ADMIN", font=("Arial 15 bold")).place(x=430, y=240)

    l4 = Label(adminlogin, text="ID", font=("Arial 12")).place(x=320, y=320)
    l5 = Label(adminlogin, text="Password", font=("Arial 12")).place(x=320, y=360)

    id_value = IntVar()
    pass_value = StringVar()

    # Entry
    id_entry = Entry(adminlogin, font=('helvetica 12'), textvariable=id_value).place(x=450, y=320)
    pass_entry = Entry(adminlogin, font=('helvetica 12'), textvariable=pass_value, show='*').place(x=450, y=360)

    def admininterface():
        global root1
        root1 = tk.Toplevel(adminlogin)  # Create Toplevel window associated with the root window
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
        b1 = Button(root1, text="  Registered \n Patients  ", image=pat_img_tk, compound=LEFT, bg="pink",
                    font=("Arial 18"), command=registered_patient)
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
        con_val = StringVar(value='10')  # Initialize with an empty string
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
                if not is_valid_contact(con_val.get()):
                    messagebox.showerror("Error", "Contact number should be a 10-digit number.")
                    return
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
                        name_val.get(), email_val.get(), con_val.get(), height_val.get(), weight_val.get(),
                        blood_val.get(),
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
            con_val = StringVar()
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
            Button(root4, text=" Close ", borderwidth=3, font=("Helvetica 14 bold"), command=root.quit).place(x=750,
                                                                                                              y=510)
            Button(root4, text=" Save ", borderwidth=3, font=("Helvetica 14 bold"), command=save_data).place(x=900,
                                                                                                             y=510)

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
        #table.heading('actions', text='Actions')  # Empty column for actions
        table.pack(fill='both', expand=True)

        root2.mainloop()

    # Button
    b1 = Button(adminlogin, text=" Login ", font=("helvetica 13 bold"), borderwidth=2, command=login).place(x=420, y=430)

    adminlogin.mainloop()
def Flip(): # PatientLogin
    global patient_window, name_val, email_val, con_val, height_val, weight_val, blood_val, add_val, dob_val
    patient_window = tk.Toplevel()
    patient_window.geometry("900x550")
    patient_window.maxsize(900, 550)
    patient_window.minsize(900, 550)
    patient_window.title("")

    # icon
    patient_window.iconbitmap("hos.ico")

    l1 = Label(patient_window, text="").pack()
    l2 = Label(patient_window, text="Clinic Management System", font=("Helvetica 20 bold")).pack()

    pat_img = Image.open('patient.png').resize((125, 125))
    pat_img_tk = ImageTk.PhotoImage(pat_img)

    ad_img = tk.Label(patient_window, image=pat_img_tk)
    ad_img.place(x=400, y=100)

    l3 = Label(patient_window, text="PATIENT", font=("Arial 15 bold")).place(x=420, y=240)

    l4 = Label(patient_window, text="ID", font=("Arial 12")).place(x=320, y=320)
    l5 = Label(patient_window, text="Password", font=("Arial 12")).place(x=320, y=360)

    id_value = IntVar()
    pass_value = StringVar()

    # Entry
    id_entry = (Entry(patient_window, font=('helvetica 12'), textvariable=id_value))
    id_entry.place(x=450, y=320)
    pass_entry = (Entry(patient_window, font=('helvetica 12'), textvariable=pass_value, show='*'))
    pass_entry.place(x=450, y=360)

    # Define global variables for entry fields
    name_val = StringVar()
    email_val = StringVar()
    con_val = IntVar()
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
        patient_window.destroy()
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
            root5.destroy()
            global root6
            root6 = tk.Toplevel()  # Create a Toplevel window as a child of root5

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

            def update_date():
                global current_date
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
                    time = values[3]

                    # Sample SQL query to insert appointment data into the pat_history table
                    sql = "INSERT INTO pat_history (Dr_name, date, time) VALUES (%s, %s, %s)"
                    values = (Dr_name, current_date, time)  # Use current_date instead of date_label.cget("text")
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
            update_date()  # Call update_date to start updating date

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
            root5.destroy()
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

        b1 = Button(f1, text="Book Appointment", font=('Helvetica 13 bold'), fg='red', bg='lavender', borderwidth=2,
                    command=BookApp)
        b1.pack(side=RIGHT, padx=10)
        b2 = Button(f1, text="History", font=('Helvetica 13 bold'), fg='black', bg='lavender', borderwidth=2,
                    command=Pat_History)
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

    # Button
    b1 = Button(patient_window, text=" Login ", font=("helvetica 13 bold"), borderwidth=2, command=Navigate).place(x=420, y=430)

    patient_window.mainloop()


def Click():  # DoctorLogin
    global root11, id_entry, pass_entry
    root11 = Toplevel()
    root11.geometry("900x550")
    root11.maxsize(900, 550)
    root11.minsize(900, 550)
    root11.title("")

    # icon
    root11.iconbitmap("hos.ico")

    l1 = Label(root11, text="")
    l1.pack()
    l2 = Label(root11, text="Clinic Management System", font=("Helvetica 20 bold"))
    l2.pack()

    doc_img = Image.open('doctor.png').resize((125, 125))
    doc_img_tk = ImageTk.PhotoImage(doc_img)

    ad_img = Label(root11, image=doc_img_tk)
    ad_img.place(x=400, y=100)

    l3 = Label(root11, text="DOCTOR", font=("Arial 15 bold"))
    l3.place(x=420, y=240)

    l4 = Label(root11, text="ID", font=("Arial 12"))
    l4.place(x=320, y=320)
    l5 = Label(root11, text="Password", font=("Arial 12"))
    l5.place(x=320, y=360)

    id_value = IntVar()
    pass_value = StringVar()

    # Entry
    id_entry = Entry(root11, font=('helvetica 12'), textvariable=id_value)
    id_entry.place(x=450, y=320)
    pass_entry = Entry(root11, font=('helvetica 12'), textvariable=pass_value, show='*')
    pass_entry.place(x=450, y=360)

    def doctor_dashboard():
        root11.destroy()
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
        l3 = Label(f1, text="Doctor Dashboard", font=("helventica 20 bold"), bg="royal blue")
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
            root8.destroy()
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
            root8.destroy()
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
                    mycursor.execute(
                        "SELECT pat_name, pat_id FROM patient")  # Modify the query as per your database schema

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
            table = ttk.Treeview(root10, columns=('1', '2'), show='headings')  # Remove the '3' column
            table.heading('1', text='Name')
            table.heading('2', text='ID')
            table.pack(fill=BOTH, expand=True)

            # Populate the Treeview initially
            populate_table()

            def prescribe_selected():
                root10.destroy()
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
                        doctor_name = "Karan"  # Update this with the actual doctor's name
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
                fetch_data_button = Button(root14, text="Fetch Patient Data", font=('Helvetica 12 bold'),
                                           command=fetch_patient_data)
                fetch_data_button.place(x=250, y=450)

                root14.mainloop()

            # Button to prescribe
            prescribe_button = Button(root10, text="Prescribe", command=prescribe_selected)
            prescribe_button.pack()

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

    # Button
    b1 = Button(root11, text=" Login ", font=("helvetica 13 bold"), borderwidth=2, command=login)
    b1.place(x=420, y=430)

    root11.mainloop()


#Buttons
b1 = Button(root, text="Doctor", font=("Arial 13"), image=doc_img_tk, compound=TOP, command=Click)
b1.pack(side=LEFT, padx=60)

b2 = Button(root, text="Patient", font=("Arial 13"), image=pat_img_tk, compound=TOP, command=Flip)
b2.pack(side=LEFT, padx=60)

b3 = Button(root, text="Admin", font=("Arial 13"), image=admin_img_img_tk, compound=TOP, command=Leaf)
b3.pack(side=LEFT, padx=60)






root.mainloop()

