from tkinter import *
import sqlite3
import tkinter.messagebox as msg
from tkinter import ttk #themed tkinter




window = Tk()
window.geometry('1500x1000')
reg_image = PhotoImage(file = 'registerbg.png')
bg_label = Label(window,image = reg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
window.title ('Search Medicine - Medicine Management System')
window.iconbitmap('icon.ico')
TopHeadingFrame = Frame(window,width=1300,bd=1)
TopHeadingFrame.pack(side = TOP)
Headinglabel = Label(TopHeadingFrame,text='Medicine Management System - Search Medicine',
                     font=('Helvetica',24),fg='yellow',bg='black')
Headinglabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window,width=700,bd=1)
MidFrame.pack(side = TOP)
#####################################################
medicine_name = StringVar()
medicine_name.set('')
medicine_namelabel = Label(MidFrame,text='Medicine Name',
                     font=('Helvetica',16),fg='orange',bg='black')
medicine_namelabel.grid(row=1,column=0,padx=10,pady=10)
medicine_nameTextBox = Entry(MidFrame,font = ('Helvetica',16),textvariable=medicine_name)
medicine_nameTextBox.grid(row=1,column=1,padx=10,pady=10)

###############################################
def back():
    window.destroy()
    import home

################################
def search():
    for i in tv.get_children():
        tv.delete(i)

    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    Medicine_name = str(medicine_name.get())
    cursor.execute("select * from 'medicine' where MedicineName=?",(Medicine_name,))
    data = cursor.fetchall()
    for  i in data:
        tv.insert("",'end',values=(i))

    cursor.close()
    conn.commit()
####################################################################

search_btn = Button(MidFrame,text='search',command=search,
                   font=('Helvetica',18),fg='black',bg='red')
search_btn.grid(row=1,column=2,padx=10,pady=10)

################################################################################
Back_btn = Button(MidFrame,text='Back',command=back,
                   font=('Helvetica',18),fg='black',bg='red')
Back_btn.grid(row=1,column=3,padx=10,pady=10)

##########################################################################


view_Frame = Frame(window, width = 400,bd=1)
view_Frame.pack(side=TOP)

tv = ttk.Treeview(view_Frame,columns=('MedicineName','MedicineID','Brand','ChemicalComponent','MFG_Date','EXP_Date','price'))


tv.heading('#1',text='MedicineName')
tv.heading('#2',text='MedicineID')
tv.heading('#3',text='Brand')
tv.heading('#4',text='ChemComp')
tv.heading('#5',text='MFG')
tv.heading('#6',text='EXP')
tv.heading('#7',text='Price')

tv.column('#0',width=0,stretch=NO)
tv.column('#1',width=50)
tv.column('#2',width=50)
tv.column('#3',width=50)
tv.column('#4',width=50)
tv.column('#5',width=50)
tv.column('#6',width=50)
tv.column('#7',width=50)

tv.pack()


window.mainloop()