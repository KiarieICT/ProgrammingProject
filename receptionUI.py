from tkinter import *
from tkinter import messagebox
import mysql.connector

root=Tk()
root.title("Patient Management")
root.geometry("1000x550+100+30")
root.config(bg="#87ceeb")

root.resizable(False,False)
#icon_image=PhotoImage(file="images/hospital.png")
#root.iconphoto(False,icon_image)

fonttype="georgia,14"
background="lightblue"

manager=LabelFrame(root,bg=background,height=550,width=996)
manager.place(x=2,y=2)

header=Label(manager,text="Escarpment Lifecare Patient Registration",bg=background,font=('georgia',18))
header.place(x=300,y=30)

dataFrame=LabelFrame(root,bg=background,height=380,width=760,font="arial")
dataFrame.place(x=120,y=80)



fname=Label(dataFrame,text="First name", font=fonttype,bg=background)
fname.place(x=120,y=50)
fname_entry=Entry(dataFrame)
fname_entry.place(x=100,y=80)

surname=Label(dataFrame,text="Surname", font=fonttype,bg=background)
surname.place(x=320,y=50)
surname_entry=Entry(dataFrame)
surname_entry.place(x=300,y=80)

lname=Label(dataFrame,text="Last name", font=fonttype,bg=background)
lname.place(x=520,y=50)
lname_entry=Entry(dataFrame)
lname_entry.place(x=500,y=80)

gender=Label(dataFrame,text="Gender", font=fonttype,bg=background)
gender.place(x=120,y=130)

options=[
    "Male",
    "Female"
]
var=StringVar()
var.set(options[0])

gender_entry=OptionMenu(dataFrame,var,*options)
gender_entry.place(x=110,y=160)

age=Label(dataFrame,text="Age", font=fonttype,bg=background)
age.place(x=320,y=130)
age_entry=Entry(dataFrame)
age_entry.place(x=300,y=160)


contacts=Label(dataFrame,text="Contacts", font=fonttype,bg=background)
contacts.place(x=520,y=130)
contacts_entry=Entry(dataFrame)
contacts_entry.place(x=500,y=160)

IDno=Label(dataFrame,text="ID number", font=fonttype,bg=background)
IDno.place(x=120,y=210)
IDno_entry=Entry(dataFrame)
IDno_entry.place(x=100,y=240)


address=Label(dataFrame,text="Address", font=fonttype,bg=background)
address.place(x=320,y=210)
address_entry=Entry(dataFrame)
address_entry.place(x=300,y=240)

blood=Label(dataFrame,text="Blood Group", font=fonttype,bg=background)
blood.place(x=520,y=210)
blood_entry=Entry(dataFrame)
blood_entry.place(x=500,y=240)

def register_patient():
    firstname=fname_entry.get()
    surname=surname_entry.get()
    lastname=lname_entry.get()
    selectedGender=var.get()
    age=age_entry.get()
    contacts=contacts_entry.get()
    Identity=IDno_entry.get()
    address=address_entry.get()
    bloodType=blood_entry.get()

    try:
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd='@Dani2031',
                database='EscarpmentDispensary'

        )

        cursor=conn.cursor()
        command = "INSERT INTO patients (firstname, surname, lastname, gender, age, contacts, identity, address, bloodType) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(command,(firstname,surname,lastname,selectedGender,age,contacts,Identity,address,bloodType))
        conn.commit()

        messagebox.showinfo("Success!","Patient information recorded successifully")

    except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to register user: {error}")
    finally:
          if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close() 




register=Button(dataFrame,text="register",width=25,command=register_patient)
register.place(x=70,y=290)

edit=Button(dataFrame,text="Edit Record",width=25)
edit.place(x=285,y=290)

appointment=Button(dataFrame,text="Book Appointment", width=25)
appointment.place(x=500,y=290)




def logout():
    root.destroy()
    import layout


logout_button=Button(manager,text="Logout",width=20,command=logout)
logout_button.place(x=800,y=500)







root.mainloop()