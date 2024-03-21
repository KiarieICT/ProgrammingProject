from tkinter import *
from admin import *
import mysql.connector
from tkinter import messagebox
from receptionUI import *

color="lightblue"
font_size=('Arial Bold',10)





class signup:
    def __init__(self,main):

        self.main=main


        signup_window=Frame(main,padx=90,pady=30,bg=color,height=430, width=800,border=0)
        signup_window.place(y=50,x=100)

        user_details=LabelFrame(signup_window,border=1,width=500,height=350,bg=color)
        user_details.place(x=60,y=9)
#      first name
        self.signup_title=Label(user_details,text="New User Registration ", bg=color,font=('georgia',14))
        self.signup_title.place(x=145,y=5)
        
        self.fname=Label(user_details,text="first name", bg=color,font=font_size)
        self.fname.place(x=125,y=55)

        self.fname_entry=Entry(user_details)
        self.fname_entry.place(x=205,y=55)

#      sirname
        
        self.surname=Label(user_details,text="surname",bg=color,font=font_size)
        self.surname.place(x=125,y=85)

        self.surname_entry=Entry(user_details)
        self.surname_entry.place(x=205,y=85)


        #username
  
        self.username=Label(user_details,text="ID Number",bg=color,font=font_size)
        self.username.place(x=125,y=115)

        self.username_entry=Entry(user_details)
        self.username_entry.place(x=205,y=115)


        #  phone number

        self.phone_number=Label(user_details,text="contacts",bg=color,font=font_size)
        self.phone_number.place(x=125,y=145)

        self.phone_number_entry=Entry(user_details)
        self.phone_number_entry.place(x=205,y=145)


        #   password


        self.password=Label(user_details,text="password",bg=color,font=font_size)
        self.password.place(x=125,y=175)

        self.password_entry=Entry(user_details,show="*")
        self.password_entry.place(x=205,y=175)

        #   password confirmation

        self.confirm_password=Label(user_details,text="confirm \n password",bg=color,font=font_size)
        self.confirm_password.place(x=122,y=200)

        self.confirm_password_entry=Entry(user_details,show="*")
        self.confirm_password_entry.place(y=210,x=205)


        # department
        self.department=Label(user_details,text="Department",bg=color,font=font_size)
        self.department.place(x=125,y=242)

        self.department_entry=Entry(user_details)
        self.department_entry.place(y=242,x=205)

        #admin password

        self.admincode=Label(user_details,text="admin\npassword",bg=color,font=font_size)
        self.admincode.place(x=125,y=270)

        self.admincode_entry=Entry(user_details)
        self.admincode_entry.place(x=205,y=275)

        # signup button

        self.register=Button(user_details,text="Register",bg=color, width=10, command=self.register_user)
        self.register.place(x=205,y=310)



        # user with account
        self.have_account=Label(signup_window,text="Already have an account?",bg=color,font=font_size)
        self.have_account.place(x=185,y=360)

        self.loginbtn=Button(signup_window,text="Login",bg=color, font=font_size,border=0,command=self.loginview)
        self.loginbtn.place(x=360,y=360)


    def register_user(self):
        firstname = self.fname_entry.get()
        lastname = self.surname_entry.get()
        username = self.username_entry.get()
        contacts = self.phone_number_entry.get()
        code = self.password_entry.get()
        confirmCode = self.confirm_password_entry.get()
        role = self.department_entry.get()
        adminPasswd = self.admincode_entry.get()

        try:
        # Creating a connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd='@Dani2031',
                database='EscarpmentDispensary'
            )

            cursor = conn.cursor()

            if code != confirmCode:
                messagebox.showwarning("Error", "Password didn't match")
            elif adminPasswd != "1354": 
                messagebox.showwarning("Warning", "Invalid admin password")
            else:
                # Insert into users table
                cursor.execute("INSERT INTO users (username, department, passcode) VALUES (%s, %s, %s)",
                               (username, role, code))
                conn.commit()

                # Insert into respective role table
                if role.lower() == "doctor":
                    cursor.execute("INSERT INTO doctor (firstname, surname, id_number, contacts) VALUES (%s, %s, %s, %s)",
                                   (firstname, lastname, username, contacts))
                elif role.lower() == "pharmacist":
                    cursor.execute("INSERT INTO pharmacist (firstname, surname, id_number, contacts) VALUES (%s, %s, %s, %s)",
                               (firstname, lastname, username, contacts))
                elif role.lower() == "receptionist":
                    cursor.execute("INSERT INTO reception (firstname, surname, id_number, contacts) VALUES (%s, %s, %s, %s)",
                               (firstname, lastname, username, contacts))
                else:
                    messagebox.showerror("Error", "Invalid role specified")

                conn.commit()
                messagebox.showinfo("Success", "Registration successful!")

                #clear the entry fields
                self.fname_entry.delete(0,END)
                self.surname_entry.delete(0,END)
                self.username_entry.delete(0,END)
                self.phone_number_entry.delete(0,END)
                self.password_entry.delete(0,END)
                self.confirm_password_entry.delete(0,END)
                self.department_entry.delete(0,END)
                self.admincode_entry.delete(0,END)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to register user: {error}")

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close() 

        # the login view
    def loginview(self):
        self.login_instance=login(self.main)

    


    #     LOGIN CLASS



class login:
    
    def __init__(self,main):
        self.main=main
        login_window=Frame(main,bg=color,height=430, width=800,border=0)
        login_window.place(y=50,x=100)

        credentials=LabelFrame(login_window,bg=color,border=1,width=400,height=190)
        credentials.place(x=200,y=90)

#   username
        self.username=Label(credentials,text="Username",bg=color,font=font_size)
        self.username.place(x=70,y=50)

        self.username_entry=Entry(credentials)
        self.username_entry.place(x=150,y=50)

#     password
        self.Password=Label(credentials,text="Password",bg=color,font=font_size)
        self.Password.place(x=70,y=80)

        self.Password_entry=Entry(credentials, show="*")
        self.Password_entry.place(x=150,y=80)

#      get in
        self.signin_btn=Button(credentials,text="login",width=10,command=self.authenticate)
        self.signin_btn.place(x=150,y=110)


#      no account user redirect
        self.no_account=Label(login_window,text="Don't have an account?",bg=color,font=font_size)
        self.no_account.place(x=270,y=295)

        self.signupbtn=Button(login_window,text="add new user",bg=color, border=0,font=font_size,command=self.signupview)
        self.signupbtn.place(y=295,x=445)
    

    def authenticate(self):
        username=self.username_entry.get()
        password=self.Password_entry.get()

        try:
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd='@Dani2031',
                database='EscarpmentDispensary'
            )
            cursor=conn.cursor()
            
            command="SELECT department FROM users WHERE username=%s AND BINARY passcode=%s"
            cursor.execute(command,(username,password))
            result=cursor.fetchone()

            if result:
                department=result[0]
                if department == "admin":
                   self.home_instance=home_page(self.main)
                elif department == "receptionist":
                    self.receptioninstance=receptionUX(self.main)
                elif department =="doctor":
                    self.main.destroy
                    import doctorUI
                    
                else:
                    messagebox.showwarning("Warning!!","no interface for you😭")
                self.username_entry.delete(0,END)
                self.Password_entry.delete(0,END)

            else:
                messagebox.showerror("Error","Invalid username or password")

        except mysql.connector.Error as e:
            messagebox.showerror("Error",f"error: {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()






#  call the home class page
    def homeview(self):
        self.home_instance=home_page(self.main)


#  call the signup page
    def signupview(self):
        self.signup_instance=signup(self.main)
    

        





