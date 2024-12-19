from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector
from tkinter import ttk
import customtkinter as ctk

root = Tk()

root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("")

#icon
root.iconbitmap("hos.ico")


def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Enter your MySQL username
            passwd="your_password",  # Enter your MySQL password
            database="your_database"  # Enter your database name
        )
        return mydb
    except mysql.connector.Error as err:
        print("Error:", err)
        return None


# Function to insert patient details into the database
def insert_patient_details():
    name = name_val.get()
    email = email_val.get()
    contact = con_val.get()
    height = height_val.get()
    weight = weight_val.get()
    blood_group = blood_val.get()
    address = add_val.get()
    dob = dob_val.get()

    try:
        mydb = connect_to_database()
        if mydb:
            cursor = mydb.cursor()
            sql = "INSERT INTO patients (name, email, contact, height, weight, blood_group, address, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, email, contact, height, weight, blood_group, address, dob)
            cursor.execute(sql, val)
            mydb.commit()
            print("Patient details inserted successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if mydb:
            mydb.close()

l0 = Label(root, text="", font=("arial 16")).pack()
f1 = Frame(root, bg='lavender')
f1.pack(fill=X)
l1 = Label(f1, text=" Profile", font=("Arial 20 bold"), fg='purple', bg='lavender')
l1.pack(side=LEFT)

b1 = Button(f1, text="Book Appointment", font=('Helvetica 13 bold'), fg='red', bg='lavender', borderwidth=2, command=insert_patient_details)
b1.pack(side=RIGHT, padx=10)
b2 = Button(f1, text="History", font=('Helvetica 13 bold'), fg='black', bg='lavender', borderwidth=2)
b2.pack(side=RIGHT, padx=10)

#patient icon
pat_img = Image.open('patient.png').resize((100,100))
pat_img_tk = ImageTk.PhotoImage(pat_img)
ad_img = tk.Label(root, image=pat_img_tk)
ad_img.place(x=40, y=80)


l1 = Label(root, text=" Name:", font=("Arial 16"))
l1.place(x=350, y=120)
name_val = StringVar()
e1 = Entry(root, textvariable=name_val).place(x=450, y=125)

l2 = Label(root, text="Patient Details", font=("Arial 16"))
l2.place(x=20, y=190)

l3 = Label(root, text="ID:", font=("Arial 16"))
l3.place(x=390, y=160)
id_val = IntVar()
e2 = Entry(root, textvariable=id_val).place(x=450, y=165)

l4 = Label(root, text="Email:", font=("Arial 16"))
l4.place(x=360, y=200)
l5 = Label(root, text="Contact:", font=("Arial 16"))
l5.place(x=340, y=240)
l6 = Label(root, text="Height:", font=("Arial 16"))
l6.place(x=355, y=280)
l7 = Label(root, text="Weight:", font=("Arial 16"))
l7.place(x=350, y=320)
l8 = Label(root, text="Blood Group:", font=("Arial 16"))
l8.place(x=302, y=360)
l9 = Label(root, text="Address:", font=("Arial 16"))
l9.place(x=343, y=400)
l10 = Label(root, text="D.O.B:", font="Arial 16")
l10.place(x=365, y=440)

email_val = StringVar()
add_val = StringVar()
con_val = IntVar()
height_val = IntVar()
weight_val = IntVar()
blood_val = StringVar()
dob_val = IntVar()

#entry
e4 = Entry(root, textvariable=email_val).place(x=450, y=205)
e5 = Entry(root, textvariable=con_val).place(x=450, y=245)
e6 = Entry(root, textvariable=height_val).place(x=450, y=285)
e7 = Entry(root, textvariable=weight_val).place(x=450, y=325)
e8 = Entry(root, textvariable=blood_val).place(x=450, y=365)
e9 = Entry(root, textvariable=add_val).place(x=450, y=405)
e10 = Entry(root, textvariable=dob_val).place(x=450, y=445)


root.mainloop()