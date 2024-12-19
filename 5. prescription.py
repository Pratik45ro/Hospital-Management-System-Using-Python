from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user="root", password="", database="clinic")
mycursor = mydb.cursor()

root = tk.Tk()

# Icon
root.iconbitmap("hos.ico")

l1 = Label(root, text="", font=('arial 14'))
l1.pack()
l2 = Label(root, text="", font=('arial 14'))
l2.pack()

root.geometry("900x550")
root.maxsize(900, 550)
root.minsize(900, 550)

f1 = Frame(root)
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
l1 = Label(root, text='Name', font=('helvetica 13'))
l1.place(x=200, y=50)
e1 = Entry(root, textvariable=name_val)
e1.place(x=300, y=50)

l2 = Label(root, text='Id', font=('helvetica 13'))
l2.place(x=200, y=100)
e2 = Entry(root, textvariable=id_val)
e2.place(x=300, y=100)

l3 = Label(root, text='Age', font=('helvetica 13'))
l3.place(x=200, y=150)
e3 = Entry(root, textvariable=age_val)
e3.place(x=300, y=150)

l4 = Label(root, text='Height', font=('helvetica 13'))
l4.place(x=520, y=50)
e4 = Entry(root, textvariable=height_val)
e4.place(x=650, y=50)

l5 = Label(root, text='Weight', font=('helvetica 13'))
l5.place(x=520, y=100)
e5 = Entry(root, textvariable=weight_val)
e5.place(x=650, y=100)

l6 = Label(root, text='Blood Group', font=('helvetica 13'))
l6.place(x=520, y=150)
e6 = Entry(root, textvariable=blood_val)
e6.place(x=650, y=150)

l7 = Label(root, text="", font=('arial 14'))
l7.pack()

l8 = Label(root, text="", font=('arial 14'))
l8.pack()

f2 = Frame(root, bg='light green')
f2.pack(fill=X)

l9 = Label(f2, text='Prescription', font=('helvetica 15 bold'), bg='light green')
l9.pack()

entry = Text(root)
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
prescribe_button = Button(root, text="Submit", font=('Helvetica 12 bold'), command=prescribe)
prescribe_button.place(x=400, y=450)

# Button to fetch patient data
fetch_data_button = Button(root, text="Fetch Patient Data", font=('Helvetica 12 bold'), command=fetch_patient_data)
fetch_data_button.place(x=250, y=450)

root.mainloop()
