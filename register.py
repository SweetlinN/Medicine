from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('1500x1000')
reg_image = PhotoImage(file = 'registerbg.png')
bg_label = Label(window,image = reg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
window.title ('Medicine Management System')
TopHeadingFrame = Frame(window,width=1300,bd=1)
TopHeadingFrame.pack(side = TOP)
Headinglabel = Label(TopHeadingFrame,text='Medicine Management System - Register',
                     font=('Helvetica',24),fg='yellow',bg='black')
Headinglabel.grid(row=0,column=0,padx=10,pady=10)
MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side = TOP)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'userdata'
(Name text,ID int,UserName text,Password text,Mobile text,Email text)""")
conn.commit()

name = StringVar()
name.set('')
Namelabel = Label(MidFrame,text='Name',
                     font=('Helvetica',16),fg='red',bg='black')
Namelabel.grid(row=0,column=0,padx=10,pady=10)
NameTextBox = Entry(MidFrame,font = ('Helvetica',16),textvariable=name)
NameTextBox.grid(row=0,column=1,padx=10,pady=10)

id = IntVar()
id.set('')

idlabel = Label(MidFrame,text='id',font=('Helvetica',16),
                 fg = 'red',bg='black')
idlabel.grid(row=1,column=0,padx=10,pady=10)
idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=id)
idTextBox.grid(row=1,column=1,padx=10,pady=10)


Username = StringVar()
Username.set('')
Usernamelabel = Label(MidFrame,text='User Name',font=('Helvetica',16),
                      fg = 'Orange',bg='black')
Usernamelabel.grid(row=2,column=0,padx=10,pady=10)
UsernameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=Username)
UsernameTextBox.grid(row=2,column=1,padx=10,pady=10)


Password = StringVar()
Password.set('')
Passwordlabel = Label(MidFrame,text='Password',font=('Helvetica',16),
                      fg='orange',bg='black')
Passwordlabel.grid(row=3,column=0,padx=10,pady=10)
PasswordTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=Password)
PasswordTextBox.grid(row=3,column=1,padx=10,pady=10)

Mobile = StringVar()
Mobile.set('')
Mobilelabel = Label(MidFrame,text='Mobile Number',font=('Helvetica',16),
                      fg='orange',bg='black')
Mobilelabel.grid(row=4,column=0,padx=10,pady=10)
MobileTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=Mobile)
MobileTextBox.grid(row=4,column=1,padx=10,pady=10)

Email = StringVar()
Email.set('')
Emaillabel = Label(MidFrame,text='Email',font=('Helvetica',16),
                      fg='orange',bg='black')
Emaillabel.grid(row=5,column=0,padx=10,pady=10)
EmailTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=Email)
EmailTextBox.grid(row=5,column=1,padx=10,pady=10)

def register():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'userdata'
    (Name,ID,UserName,Password,Mobile,Email) values(?,?,?,?,?,?)""",
                   (str(name.get()),str(id.get()),str(Username.get()),str(Password.get()),
                    str(Mobile.get()),str(Email.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('Confirmation','New user added',icon='info')
    else:
        msg.showinfo('Error','New user not added',icon='warning')

def Login():
    window.destroy()
    import Login







Submit_btn = Button(MidFrame,text='SUBMIT',command=register,
                    font=('Helvetica',18),fg='black',bg='green')
Submit_btn.grid(row=6,column=1,padx=10,pady=10)


AlreadyUserlabel = Label(MidFrame,text='Already a user?',font=('Helvetica',16),
                         fg='orange',bg='black')
AlreadyUserlabel.grid(row=7,column=0,padx=10,pady=10)


Login_btn = Button(MidFrame,text='Login',command=Login,
                   font=('Helvetica',18),fg='black',bg='red')
Login_btn.grid(row=7,column=1,padx=10,pady=10)




window.mainloop()

