from tkinter import *
from users import *
import subprocess

root=Tk()
root.title("Dispensary system")
root.geometry("1000x550+100+30")
root.config(bg="#87ceeb")

root.resizable(False,False)
#icon_image=PhotoImage(file="images/hospital.png")
#root.iconphoto(False,icon_image)


def logout():
    root.destroy()
    import layout


logout_button=Button(root,text="Logout",width=20,command=logout)
logout_button.place(x=800,y=500)






root.mainloop()