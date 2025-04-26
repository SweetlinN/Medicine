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
Headinglabel = Label(TopHeadingFrame,text='Medicine Management System - Login',
                     font=('Helvetica',24),fg='yellow',bg='black')
Headinglabel.grid(row=0,column=0,padx=10,pady=10)


MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side = TOP)
Username = StringVar()
Username.set('')
Usernamelabel = Label(MidFrame,text='User Name',font=('Helvetica',16),
                      fg = 'Orange',bg='black')
Usernamelabel.grid(row=0,column=0,padx=10,pady=10)
UsernameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=Username)
UsernameTextBox.grid(row=0,column=1,padx=10,pady=10)


Password = StringVar()
Password.set('')
Passwordlabel = Label(MidFrame,text='Password',font=('Helvetica',16),
                      fg='orange',bg='black')
Passwordlabel.grid(row=1,column=0,padx=10,pady=10)
PasswordTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=Password)
PasswordTextBox.grid(row=1,column=1,padx=10,pady=10)

def register():
    window.destroy()
    import register
def Login():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""select * from 'userdata' where
    UserName = ? and Password = ?""",(Username.get(),Password.get()))
    if len(list(cursor.fetchall())) >0:
        msg.showinfo('Login confirmation','Login successful',icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo('Login Error','User not defined',icon='warning')


Submit_btn = Button(MidFrame,text='Register',command=register,
                    font=('Helvetica',18),fg='black',bg='green')
Submit_btn.grid(row=3,column=1,padx=10,pady=10)


NotUserlabel = Label(MidFrame,text='Not a user yet?',font=('Helvetica',16),
                         fg='orange',bg='black')
NotUserlabel.grid(row=3,column=0,padx=10,pady=10)


Login_btn = Button(MidFrame,text='Login',command=Login,
                   font=('Helvetica',18),fg='black',bg='red')
Login_btn.grid(row=2,column=1,padx=10,pady=10)


window.mainloop()