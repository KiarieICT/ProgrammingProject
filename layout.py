from tkinter import *
from users import *
import customtkinter as ctk

ctk.set_appearance_mode("Light")
root=Tk()
root.geometry("1000x550+100+30")
root.config(bg="#87ceeb")

root.resizable(False,False)
icon_image=PhotoImage(file="images/hospital.png")
root.iconphoto(False,icon_image)

login_page=login(root)




root.mainloop()