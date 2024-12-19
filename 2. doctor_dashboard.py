from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
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
l3 = Label(f1, text="Dashboard", font=("helventica 20 bold"), bg="royal blue")
l3.pack()

dash_img = Image.open('dashboard.png').resize((50,50))
dash_img_tk = ImageTk.PhotoImage(dash_img)

pat_img = Image.open("tpatients.png").resize((50,50))
pat_img_tk = ImageTk.PhotoImage(pat_img)

app_img = Image.open('appointment.png').resize((50,50))
app_img_tk = ImageTk.PhotoImage(app_img)

dash_img_label = Label(image=dash_img_tk, bg="royal blue")
dash_img_label.place(x=310, y=44)

# Buttons
b1 = Button(root, text=" Total Patients ", image=pat_img_tk, compound=LEFT, bg='pink', font=("Arial 18"), borderwidth=2)
b1.pack(side=LEFT, padx=60)

b2 = Button(root, text=" Appointments ", image=app_img_tk, compound=LEFT, bg='red', font=("Arial 18"), borderwidth=2)
b2.pack(side=LEFT, padx=60)




root.mainloop()