from tkinter import *
from tkinter import messagebox
import mysql.connector

fonttype="georgia,14"
background="lightblue"

class receptionUX:
     def __init__(self,main):
        self.main=main
        main.title("patient management")
        manager=Frame(main,bg=background,height=550,width=996)
        manager.place(x=2,y=2)

        self.header=Label(manager,text="Escarpment Lifecare Patient Registration",bg=background,font=('georgia',18))
        self.header.place(x=300,y=30)

        self.dataFrame=Frame(manager,bg=background,height=380,width=760)
        self.dataFrame.place(x=120,y=80)



        self.fname=Label(self.dataFrame,text="First name", font=fonttype,bg=background)
        self.fname.place(x=120,y=50)
        self.fname_entry=Entry(self.dataFrame)
        self.fname_entry.place(x=100,y=80)

        self.surname=Label(self.dataFrame,text="Surname", font=fonttype,bg=background)
        self.surname.place(x=320,y=50)
        self.surname_entry=Entry(self.dataFrame)
        self.surname_entry.place(x=300,y=80)

        self.lname=Label(self.dataFrame,text="Last name", font=fonttype,bg=background)
        self.lname.place(x=520,y=50)
        self.lname_entry=Entry(self.dataFrame)
        self.lname_entry.place(x=500,y=80)

        self.gender=Label(self.dataFrame,text="Gender", font=fonttype,bg=background)
        self.gender.place(x=120,y=130)

        options=[
            "Select",
            "Male",
            "Female"
        ]
        var=StringVar()
        var.set(options[0])

        self.gender_entry=OptionMenu(self.dataFrame,var,*options)
        self.gender_entry.place(x=110,y=160)

        self.age=Label(self.dataFrame,text="Age", font=fonttype,bg=background)
        self.age.place(x=320,y=130)
        self.age_entry=Entry(self.dataFrame)
        self.age_entry.place(x=300,y=160)


        self.contacts=Label(self.dataFrame,text="Contacts", font=fonttype,bg=background)
        self.contacts.place(x=520,y=130)
        self.contacts_entry=Entry(self.dataFrame)
        self.contacts_entry.place(x=500,y=160)

        self.IDno=Label(self.dataFrame,text="ID number", font=fonttype,bg=background)
        self.IDno.place(x=120,y=210)
        self.IDno_entry=Entry(self.dataFrame)
        self.IDno_entry.place(x=100,y=240)


        self.address=Label(self.dataFrame,text="Address", font=fonttype,bg=background)
        self.address.place(x=320,y=210)
        self.address_entry=Entry(self.dataFrame)
        self.address_entry.place(x=300,y=240)

        self.blood=Label(self.dataFrame,text="Blood Group", font=fonttype,bg=background)
        self.blood.place(x=520,y=210)
        self.blood_entry=Entry(self.dataFrame)
        self.blood_entry.place(x=500,y=240)

        def register_patient():
            firstname=self.fname_entry.get()
            surname=self.surname_entry.get()
            lastname=self.lname_entry.get()
            selectedGender=var.get()
            age=self.age_entry.get()
            contacts=self.contacts_entry.get()
            Identity=self.IDno_entry.get()
            address=self.address_entry.get()
            bloodType=self.blood_entry.get()

            try:

                
                if all(x=="" for x in (firstname,surname,lastname,Identity,selectedGender,age,contacts,address,bloodType)):
                   messagebox.showwarning("Warning","Fill all the fields")

                else:
                    
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


                #clear the entry box after entry
                self.fname_entry.delete(0,END)
                self.lname_entry.delete(0,END)
                self.surname_entry.delete(0,END)
                self.age_entry.delete(0,END)
                self.contacts_entry.delete(0,END)
                self.IDno_entry.delete(0,END)
                self.address_entry.delete(0,END)
                self.blood_entry.delete(0,END)


            except mysql.connector.Error as error:
                    messagebox.showerror("Error", f"Failed to register user: {error}")
            finally:
                if 'conn' in locals() and conn.is_connected():
                        cursor.close()
                        conn.close() 




        self.register=Button(self.dataFrame,text="register",width=25,command=register_patient)
        self.register.place(x=70,y=290)

        self.edit=Button(self.dataFrame,text="Edit Record",width=25)
        self.edit.place(x=285,y=290)

        self.appointment=Button(self.dataFrame,text="Book Appointment", width=25)
        self.appointment.place(x=500,y=290)




        def logout():
           manager.destroy()
           
             
            


        self.logout_button=Button(manager,text="Logout",width=20,command=logout)
        self.logout_button.place(x=800,y=500)







