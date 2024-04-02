from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk


fonttype="georgia,14"
background="lightblue"
fontcolor="black"
bgcolor="White"



class receptionUX:
     def __init__(self,main):
        self.main=main
        manager=Frame(main,bg=background,height=550,width=996)
        manager.place(x=2,y=2)

        # cretaing the widgets

        self.header=ctk.CTkLabel(manager,text="Escarpment Lifecare Patient Registration",font=('georgia',25) ,text_color="Black")
        self.header.place(x=270,y=40)

        self.dataFrame=Frame(manager,bg=background,height=380,width=760)
        self.dataFrame.place(x=120,y=80)



        self.fname=Label(self.dataFrame,text="First name", font=fonttype,bg=background)
        self.fname.place(x=120,y=50)
        self.fname_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.fname_entry.focus()
        self.fname_entry.place(x=100,y=80)

        self.surname=Label(self.dataFrame,text="Surname", font=fonttype,bg=background)
        self.surname.place(x=320,y=50)
        self.surname_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.surname_entry.place(x=300,y=80)

        self.lname=Label(self.dataFrame,text="Last name", font=fonttype,bg=background)
        self.lname.place(x=520,y=50)
        self.lname_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.lname_entry.place(x=500,y=80)

        self.gender=Label(self.dataFrame,text="Gender", font=fonttype,bg=background)
        self.gender.place(x=120,y=130)


        self.gender_entry= ctk.CTkComboBox(self.dataFrame, width=140,fg_color=bgcolor,text_color=fontcolor, values=[
                                                          "Male", "Female"], state="readonly")
        self.gender_entry.set("Male")
        self.gender_entry.place(x=100,y=160)

        self.age=Label(self.dataFrame,text="Age", font=fonttype,bg=background)
        self.age.place(x=320,y=130)
        self.age_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.age_entry.place(x=300,y=160)


        self.contacts=Label(self.dataFrame,text="Contacts", font=fonttype,bg=background)
        self.contacts.place(x=520,y=130)
        self.contacts_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.contacts_entry.place(x=500,y=160)

        self.IDno=Label(self.dataFrame,text="ID number", font=fonttype,bg=background)
        self.IDno.place(x=120,y=210)
        self.IDno_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.IDno_entry.place(x=100,y=240)


        self.address=Label(self.dataFrame,text="Address", font=fonttype,bg=background)
        self.address.place(x=320,y=210)
        self.address_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.address_entry.place(x=300,y=240)

        self.blood=Label(self.dataFrame,text="Blood Group", font=fonttype,bg=background)
        self.blood.place(x=520,y=210)
        self.blood_entry=ctk.CTkEntry(self.dataFrame,fg_color=bgcolor,text_color=fontcolor)
        self.blood_entry.place(x=500,y=240)


#   register patients into the database
        def register_patient():
            firstname=self.fname_entry.get()
            surname=self.surname_entry.get()
            lastname=self.lname_entry.get()
            selectedGender=self.gender_entry.get()
            age=self.age_entry.get()
            contacts=self.contacts_entry.get()
            Identity=self.IDno_entry.get()
            address=self.address_entry.get()
            bloodType=self.blood_entry.get()

            try:

                #check if the field is empty
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



  #register patient button
        self.register=ctk.CTkButton(self.dataFrame,text="register",width=140,text_color=fontcolor,command=register_patient)
        self.register.place(x=100,y=290)



# edit patient data from the database
        def edit_patient_info():
              
               self.patient_details=Frame(self.dataFrame,width=760,height=850,bg=background, bd=1)
               self.patient_details.place(x=40,y=9)

               #editing fields
               self.info_editor=LabelFrame(self.patient_details,width=690, height=200,bg=background,text="Edit Records")
               self.info_editor.place(x=10,y=40)

               self.fn=Label(self.info_editor,text="First Name",bg=background)
               self.fn.place(x=20,y=10)
               self.fn_entry=ctk.CTkEntry(self.info_editor,width=100)
               self.fn_entry.place(x=10,y=30)

               self.sn=Label(self.info_editor,text="Sur Name",bg=background)
               self.sn.place(x=130,y=10)
               self.sn_entry=ctk.CTkEntry(self.info_editor,width=100)
               self.sn_entry.place(x=120,y=30)

               self.ln=Label(self.info_editor,text="Last Name",bg=background)
               self.ln.place(x=240,y=10)
               self.ln_entry=ctk.CTkEntry(self.info_editor,width=100)
               self.ln_entry.place(x=230,y=30)

               self.cn=Label(self.info_editor,text="Contacts",bg=background)
               self.cn.place(x=350,y=10)
               self.cn_entry=ctk.CTkEntry(self.info_editor,width=100)
               self.cn_entry.place(x=340,y=30)

               self.idn=Label(self.info_editor,text="ID Number",bg=background)
               self.idn.place(x=460,y=10)
               self.idn_entry=ctk.CTkEntry(self.info_editor,width=100)
               self.idn_entry.place(x=450,y=30)

               self.addr=Label(self.info_editor,text="Address",bg=background)
               self.addr.place(x=580,y=10)
               self.addr_entry=ctk.CTkEntry(self.info_editor,width=100)
               self.addr_entry.place(x=570,y=30)





                #styling the treeview
               self.style=ttk.Style()
               self.style.theme_use('default')

               self.style.configure('Treeview',
                                    background="#D3D3D3",
                                    foregroung='lightblue',
                                    rowheight=25,
                                    fieldbackground='#D3D3D3')
               
         #frame for the tree view
               self.record_frame=Frame(self.patient_details)
               self.record_frame.place(x=10, y=250)

        # the tree scrollbar 
               self.tree_scroll=Scrollbar(self.record_frame,bg=background)
               self.tree_scroll.pack(side=RIGHT,fill=Y)

        
        #creating the tree view
               self.patientTree=ttk.Treeview(self.record_frame,height=4,yscrollcommand=self.tree_scroll.set,selectmode=EXTENDED)
               #configure the scrollbar
               self.tree_scroll.config(command=self.patientTree.yview)

               self.patientTree['columns']=("Firstname", "Surname", "Lastname","Contacts","ID Number","Address",)
               #format the columns
               self.patientTree.column("#0",width=0,stretch=NO)
               self.patientTree.column("Firstname",anchor=CENTER,width=120)
               self.patientTree.column("Surname",anchor=CENTER,width=120)
               self.patientTree.column("Lastname",anchor=CENTER,width=120)
               self.patientTree.column("Contacts",anchor=CENTER,width=80)
               self.patientTree.column("ID Number",anchor=CENTER,width=80)
               self.patientTree.column("Address",anchor=CENTER,width=100)

               #headings
               self.patientTree.heading("#0",text="")
               self.patientTree.heading("Firstname",text="First Name",anchor=CENTER)
               self.patientTree.heading("Surname",text="SurName",anchor=CENTER)
               self.patientTree.heading("Lastname",text="Last Name",anchor=CENTER)
               self.patientTree.heading("Contacts",text="Contacts",anchor=CENTER)
               self.patientTree.heading("ID Number",text="ID Number",anchor=CENTER)
               self.patientTree.heading('Address', text="Address",anchor=CENTER)

               #create striped rows

               self.patientTree.tag_configure('oddrow',background="white")
               self.patientTree.tag_configure('evenrow',background="lightblue")

               

               self.conn = mysql.connector.connect(
                        host="localhost",
                            user="root",
                        passwd='@Dani2031',
                        database='EscarpmentDispensary'
        
                )
                
               self.cursor=self.conn.cursor()
               self.command="SELECT firstname, surname, lastname,contacts, identity, address FROM patients"
               self.cursor.execute(self.command)
               rows=self.cursor.fetchall()

               count=0
                # insert the rows into tree view
               for record in rows:
                    if count%2==0:
                         
                        self.patientTree.insert("",index="end",text="",values=(record[0],record[1],record[2],record[3],record[4],record[5]),
                                                tags=('evenrow',))
                    else:
                         
                         self.patientTree.insert("",index="end",text="",values=(record[0],record[1],record[2],record[3],record[4],record[5]),
                                                tags=('oddrow',))
                         
                    count+=1
                    self.patientTree.pack()

               def select_record(event):
                    self.fn_entry.delete(0,END)
                    self.sn_entry.delete(0,END)
                    self.ln_entry.delete(0,END)
                    self.cn_entry.delete(0,END)
                    self.idn_entry.delete(0,END)
                    self.addr_entry.delete(0,END)

                    #grab records 
                    selected=self.patientTree.focus()
                    #grab record values
                    values=self.patientTree.item(selected,'values')

                    #insert into the fields
                    self.fn_entry.insert(0,values[0])
                    self.sn_entry.insert(0,values[1])
                    self.ln_entry.insert(0,values[2])
                    self.cn_entry.insert(0,values[3])
                    self.idn_entry.insert(0,values[4])
                    self.addr_entry.insert(0,values[5])

                #bind the Patienttreeview
               self.patientTree.bind("<ButtonRelease>",select_record)


               def closeframe():
                    self.patient_details.destroy()

               self.close_frame=ctk.CTkButton(self.patient_details,text="Save Records",width=100,text_color=fontcolor,command=closeframe)
               self.close_frame.place(x=10,y=10)
  # edit patients details button

        self.edit=ctk.CTkButton(self.dataFrame,text="Edit Record",width=140, text_color=fontcolor,command=edit_patient_info)
        self.edit.place(x=300,y=290)
  #   book appointment button
        self.appointment=ctk.CTkButton(self.dataFrame,text="Book Appointment",text_color=fontcolor, width=140)
        self.appointment.place(x=500,y=290)




        def logout():
           manager.destroy()
           
             
            


        self.logout_button=ctk.CTkButton(manager,text="Logout",width=120,text_color=fontcolor,command=logout)
        self.logout_button.place(x=800,y=500)







