from tkinter import *
from PIL import Image, ImageTk

color = "white"
font_size = ('Arial', 12)


class home_page:
    def __init__(self, main):
        self.main = main
        home_window = Frame(main, bg=color, height=545, width=994)
        home_window.place(x=3, y=1)

        def logout_view():
            home_window.destroy()
            
            

        self.welcome = Label(home_window, text="Welcome To Admin Portal", bg=color, font=("georgia", 14))
        self.welcome.place(x=123, y=30)

        # underline
        self.canva = Canvas(home_window, bg="black", height=2, width=723)
        self.canva.place(x=50, y=60)

        self.canva_divider = Canvas(home_window, bg="black", height=600, width=2)
        self.canva_divider.place(x=280, y=65)

        # admin image
        self.original_admin_image = Image.open("images/admin2.png")
        self.resized_admin_image = self.original_admin_image.resize((80, 80))

        # use image with tkinter
        self.admin_image = ImageTk.PhotoImage(self.resized_admin_image)

        self.admin_image_label = Label(home_window, image=self.admin_image, bg=color)
        self.admin_image_label.place(x=13, y=2)

        # logout
        self.logout = Button(home_window, text="logout", fg="red", bg=color, border=0, font=("georgia", 11),
                             command=logout_view)
        self.logout.place(x=930, y=30)

        # NAVIGATION

        # doctors

        self.nav_div = Canvas(home_window, bg="black", width=170, height=1)

        self.original_doctor_image = Image.open("images/doctor.png")
        self.resized_doctor_image = self.original_doctor_image.resize((50, 50))
        self.doctor_image = ImageTk.PhotoImage(self.resized_doctor_image)
        self.doctor_image_label = Label(home_window, bg=color, image=self.doctor_image)
        self.doctor_image_label.place(x=80, y=75)

        self.doctor_button = Button(home_window, text="Doctors", bg=color, borderwidth=3, font=('georgia', 12),
                                    fg="Red", width=10)
        self.doctor_button.place(x=140, y=85)

        self.nav_div.place(x=75, y=127)

        # nurses

        self.nav_div2 = Canvas(home_window, bg="black", width=170, height=1)
        self.original_nurse_image = Image.open("images/nurse.png")
        self.resized_nurse_image = self.original_nurse_image.resize((50, 50))
        self.nurse_image = ImageTk.PhotoImage(self.resized_nurse_image)
        self.nurse_image_label = Label(home_window, bg=color, image=self.nurse_image)
        self.nurse_image_label.place(x=80, y=132)

        self.nurse_button = Button(home_window, text="Nurses", bg=color, borderwidth=3, font=('georgia', 12),
                                   fg="Red", width=10)
        self.nurse_button.place(x=140, y=141)

        self.nav_div2.place(x=75, y=185)

        # pharmacists

        self.nav_div3 = Canvas(home_window, bg="black", width=170, height=1)
        self.original_pharmacist_image = Image.open("images/pharmacist2.png")
        self.resized_pharmacist_image = self.original_pharmacist_image.resize((46, 46))
        self.pharmacist_image = ImageTk.PhotoImage(self.resized_pharmacist_image)
        self.pharmacist_image_label = Label(home_window, bg=color, image=self.pharmacist_image)
        self.pharmacist_image_label.place(x=80, y=193)

        self.pharmacist_button = Button(home_window, text="Pharmacists", bg=color, borderwidth=3,
                                        font=('georgia', 12), fg="Red", width=10)
        self.pharmacist_button.place(x=140, y=199)

        self.nav_div3.place(x=75, y=243)

        # receptionist
        self.nav_div4 = Canvas(home_window, bg="black", width=170, height=1)
        self.original_receptionist_image = Image.open("images/reception.png")
        self.resized_receptionist_image = self.original_receptionist_image.resize((46, 46))
        self.receptionist_image = ImageTk.PhotoImage(self.resized_receptionist_image)
        self.receptionist_image_label = Label(home_window, bg=color, image=self.receptionist_image)
        self.receptionist_image_label.place(x=80, y=251)

        self.reception_button = Button(home_window, text="Reception", bg=color, borderwidth=3, font=('georgia', 12),
                                       fg="Red", width=10)
        self.reception_button.place(x=140, y=257)

        self.nav_div4.place(x=75, y=301)

        # patients

        self.nav_div5 = Canvas(home_window, bg="black", width=170, height=1)
        self.original_patient_image = Image.open("images/patient.png")
        self.resized_patient_image = self.original_patient_image.resize((46, 46))
        self.patient_image = ImageTk.PhotoImage(self.resized_patient_image)
        self.patient_image_label = Label(home_window, bg=color, image=self.patient_image)
        self.patient_image_label.place(x=80, y=305)

        self.patient_button = Button(home_window, text="Patients", bg=color, borderwidth=3, font=('georgia', 12),
                                     fg="Red", width=10)
        self.patient_button.place(x=140, y=315)

        self.nav_div5.place(x=75, y=359)

        # medications

        self.nav_div6 = Canvas(home_window, bg="black", width=170, height=1)
        self.original_prescription_image = Image.open("images/prescription.png")
        self.resized_prescription_image = self.original_prescription_image.resize((50, 50))
        self.prescription_image = ImageTk.PhotoImage(self.resized_prescription_image)
        self.prescription_image_label = Label(home_window, bg=color, image=self.prescription_image)
        self.prescription_image_label.place(x=80, y=363)

        self.prescription_button = Button(home_window, text="Medication", bg=color, borderwidth=3,
                                          font=('georgia', 12), fg="Red", width=10)
        self.prescription_button.place(x=140, y=373)

        self.nav_div6.place(x=75, y=417)



