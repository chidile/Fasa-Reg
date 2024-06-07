from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root=Tk()
root.title("FASA Registration System")
root.geometry("1250x700+210+210")
root.config(bg=background)


file = pathlib.Path("Student_data.xlsx")
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1'] = "Rgistrtion No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date of Registrtion"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father Name"
    sheet['J1'] = "Mothers Name"
    sheet['K1'] = "Father Occupation"
    sheet['L1'] = "Mothers Occupation"

    file.save("Student_data.xlsx")


### Top Frames
Label(root,text="Email: info@fasa-international.org",width=10,height=3,bg="#f0687c",anchor="e").pack(side=TOP,fill=X)
Label(root,text="FASA ATTENDANCE",width=16,height=2,bg="#c36464",fg="#fff",font="arial 20 bold").pack(side=TOP,fill=X)


## Search Box to update
Search=StringVar()
Entry(root, textvariable=Search,width=15,bd=2,font="arial 20").place(x=820,y=70)
imageIcon3=PhotoImage(file="Images/search.png")
Srch=Button(root,text="Search",compound=LEFT,image=imageIcon3,width=123,bg='#68ddfa', font="arial 13 bold")
Srch.place(x=1060,y=66)

imageIcon4=PhotoImage(file="Images/upload.png")
Update_button=Button(root,image=imageIcon4,bg="#c36464")
Update_button.place(x=110,y=64)


## Registration and date
Label(root,text="Team No:", font="arial 13", fg=framebg,bg=background).place(x=30,y=150)
Label(root,text="Date:", font="arial 13", fg=framebg,bg=background).place(x=500,y=150)

Registration=StringVar()
Date = StringVar()

reg_entry = Entry(root,textvariable=Registration,width=15,font="arial 10")
reg_entry.place(x=160,y=150)

#Registration No
today=date.today()
d1=today.strftime("%d/%m/%Y")
date_entry=Entry(root,textvariable=Date,width=15,font="arial 10")
date_entry.place(x=550,y=150)
Date.set(d1)



##Team Details
obj=LabelFrame(root,text="Teams Details", font=20,bd=2,width=900,bg=framebg,fg=framefg,height=250,relief=GROOVE)
obj.place(x=30,y=200)

Label(obj,text="Full Name:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=50)
Label(obj,text="Date of Birth:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=100)
Label(obj,text="Gender:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=150)

Label(obj,text="Department:",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=50)
Label(obj,text="Director:",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=100)
Label(obj,text="Gender:",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=150)

Name=StringVar()
name_entry = Entry(obj,textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y=50)


radio = IntVar()
R1=Radiobutton(obj,text='Male',variable=radio, value=1, bg=framebg,fg=framefg)
R1.place(x=150,y=150)











##Team Department Details
obj2=LabelFrame(root,text="Department Details", font=20,bd=2,width=900,bg=framebg,fg=framefg,height=220,relief=GROOVE)
obj2.place(x=30,y=460)


root.mainloop()

