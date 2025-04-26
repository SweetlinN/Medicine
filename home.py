from tkinter import *
import sqlite3
import tkinter.messagebox as msg




window = Tk()
window.geometry('1500x1000')
reg_image = PhotoImage(file = 'registerbg.png')
bg_label = Label(window,image = reg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
window.title ('Medicine Management System')
window.iconbitmap('icon.ico')
TopHeadingFrame = Frame(window,width=1300,bd=1)
TopHeadingFrame.pack(side = TOP)
Headinglabel = Label(TopHeadingFrame,text='Medicine Management System - Home',
                     font=('Helvetica',24),fg='yellow',bg='black')
Headinglabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side = TOP)


def add():
    window.destroy()
    import add_medicine
add_btn = Button(MidFrame,text='ADD MEDICINE',command=add,
                   font=('Helvetica',18),fg='black',bg='green')
add_btn.grid(row=0,column=1,padx=10,pady=10)


def view():
    window.destroy()
    import view_medicine
view_btn = Button(MidFrame,text='VIEW MEDICINE',command=view,
                   font=('Helvetica',18),fg='black',bg='green')
view_btn.grid(row=1,column=1,padx=10,pady=10)

def search():
    window.destroy()
    import search_medicine

search_btn = Button(MidFrame,text='SEARCH MEDICINE',command=search,
                   font=('Helvetica',18),fg='black',bg='green')
search_btn.grid(row=2,column=1,padx=10,pady=10)


def delete():
    window.destroy()
    import delete_medicine

delete_btn = Button(MidFrame,text='DELETE MEDICINE',command=delete,
                   font=('Helvetica',18),fg='black',bg='green')
delete_btn.grid(row=3,column=1,padx=10,pady=10)



def Logout():
    window.destroy()
    import Login
Login_btn = Button(MidFrame,text='LOGOUT',command=Logout,
                   font=('Helvetica',18),fg='black',bg='red')
Login_btn.grid(row=4,column=2,padx=10,pady=10)


window.mainloop()