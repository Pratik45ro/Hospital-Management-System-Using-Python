from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()

root.geometry("1100x600")
root.maxsize(1100,600)
root.minsize(1100,600)
root.title("")

# icon
root.iconbitmap("hos.ico")

def save_data():
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
        values = (name_val.get(), email_val.get(), con_val.get(), height_val.get(), weight_val.get(), blood_val.get(), add_val.get(), id_val.get(), pass_val.get())

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
Label(root, text="  Patient", font=("Arial 20 bold"), bg='pink').pack(side=LEFT)
Label(root, text="Name", font=("Arial 16")).place(x=400, y=100)
Label(root, text="Email", font=("Arial 16")).place(x=400, y=150)
Label(root, text="Contact", font=("Arial 16")).place(x=400, y=200)
Label(root, text="Height", font=("Arial 16")).place(x=400, y=250)
Label(root, text="Weight", font=("Arial 16")).place(x=400, y=300)
Label(root, text="Blood Group", font=("Arial 16")).place(x=400, y=350)
Label(root, text="Address", font=("Arial 16")).place(x=400, y=400)
Label(root, text="ID", font=("Arial 16")).place(x=400, y=450)
Label(root, text="Password", font=("Arial 16")).place(x=400, y=500)

# Values
name_val = StringVar()
email_val = StringVar()
add_val = StringVar()
con_val = IntVar()
height_val = IntVar()
weight_val = IntVar()
blood_val = StringVar()
id_val = StringVar()
pass_val = StringVar()

# Entry fields
Entry(root, textvariable=name_val).place(x=550,y=100)
Entry(root, textvariable=email_val).place(x=550,y=150)
Entry(root, textvariable=con_val).place(x=550,y=200)
Entry(root, textvariable=height_val).place(x=550,y=250)
Entry(root, textvariable=weight_val).place(x=550,y=300)
Entry(root, textvariable=blood_val).place(x=550,y=350)
Entry(root, textvariable=add_val).place(x=550,y=400)
Entry(root, textvariable=id_val).place(x=550,y=450)
Entry(root, textvariable=pass_val).place(x=550,y=500)

# Buttons
Button(root, text=" Close ", borderwidth=3, font=("Helvetica 14 bold"), command=root.quit).place(x=750,y=510)
Button(root, text=" Save ", borderwidth=3, font=("Helvetica 14 bold"), command=save_data).place(x=900,y=510)

root.mainloop()
