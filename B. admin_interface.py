from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import mysql.connector as myconn
import customtkinter as ctk


root = Tk()

root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("")



#icon
root.iconbitmap("hos.ico")

l1 = Label(root, text="")
l1.pack()
l2 = Label(root, text="")
l2.pack()
f1 = Frame(root, bg="royal blue", borderwidth=10)
f1.pack(fill=X)
l3 = Label(f1, text="Admin Dashboard", font=("helventica 20 bold"), bg="royal blue")
l3.pack()


# importing images
doc_img = Image.open('Doctor.png').resize((50,50))
doc_img_tk = ImageTk.PhotoImage(doc_img)

pat_img = Image.open('Patient.png').resize((50,50))
pat_img_tk = ImageTk.PhotoImage(pat_img)

dash_img = Image.open('dashboard.png').resize((50,50))
dash_img_tk = ImageTk.PhotoImage(dash_img)

dash_img_label = Label(image=dash_img_tk, bg="royal blue")


app_img = Image.open('appointment.png').resize((50,50))
app_img_tk = ImageTk.PhotoImage(app_img)

#Buttons
b1 = Button(root, text="  Registered \n Patients  ", image=pat_img_tk, compound=LEFT, bg="pink", font=("Arial 18"), command=Review)
b1.pack(side=LEFT, padx=45)

b2 = Button(root, text="  Registered \n Doctors  ", image=doc_img_tk, compound=LEFT, bg="light green", font=("Arial 18"))
b2.pack(side=LEFT, padx=45)

b3 = Button(root, text=" Appointments  ", image = app_img_tk, compound=LEFT, bg="red", font=("Arial 18"))
b3.pack(side=LEFT, padx=45)







root.mainloop()