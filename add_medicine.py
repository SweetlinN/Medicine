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
Headinglabel = Label(TopHeadingFrame,text='Medicine Management System - Add Medicine',
                     font=('Helvetica',24),fg='yellow',bg='black')
Headinglabel.grid(row=0,column=0,padx=10,pady=10)
MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side = TOP)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'medicine'
(MedicineName text,MedicineId int,Brand text,ChemicalComponent text,MFG_Date text,EXP_Date text,price int)""")
conn.commit()

medicine_name = StringVar()
medicine_name.set('')
medicine_namelabel = Label(MidFrame,text='Medicine Name',
                     font=('Helvetica',16),fg='orange',bg='black')
medicine_namelabel.grid(row=0,column=0,padx=10,pady=10)
medicine_nameTextBox = Entry(MidFrame,font = ('Helvetica',16),textvariable=medicine_name)
medicine_nameTextBox.grid(row=0,column=1,padx=10,pady=10)

medicine_id = IntVar()
medicine_id.set('')

medicine_idlabel = Label(MidFrame,text='Medicine ID',font=('Helvetica',16),
                 fg = 'orange',bg='black')
medicine_idlabel.grid(row=1,column=0,padx=10,pady=10)
medicine_idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_id)
medicine_idTextBox.grid(row=1,column=1,padx=10,pady=10)


brand = StringVar()
brand.set('')
brandlabel = Label(MidFrame,text='Brand Name',font=('Helvetica',16),
                      fg = 'Orange',bg='black')
brandlabel.grid(row=2,column=0,padx=10,pady=10)
brandTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=brand)
brandTextBox.grid(row=2,column=1,padx=10,pady=10)


chemical_component = StringVar()
chemical_component.set('')
chemical_componentlabel = Label(MidFrame,text='Chemical component',font=('Helvetica',16),
                      fg='orange',bg='black')
chemical_componentlabel.grid(row=3,column=0,padx=10,pady=10)
chemical_componentTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=chemical_component)
chemical_componentTextBox.grid(row=3,column=1,padx=10,pady=10)

mfg = StringVar()
mfg.set('')
mfglabel = Label(MidFrame,text='MFG Date',font=('Helvetica',16),
                      fg='orange',bg='black')
mfglabel.grid(row=4,column=0,padx=10,pady=10)
mfgTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=mfg)
mfgTextBox.grid(row=4,column=1,padx=10,pady=10)

exp = StringVar()
exp.set('')
explabel = Label(MidFrame,text='EXP Date',font=('Helvetica',16),
                      fg='orange',bg='black')
explabel.grid(row=5,column=0,padx=10,pady=10)
expTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=exp)
expTextBox.grid(row=5,column=1,padx=10,pady=10)

price = IntVar()
price .set('')
pricelabel = Label(MidFrame,text='Price',font=('Helvetica',16),
                      fg='orange',bg='black')
pricelabel.grid(row=6,column=0,padx=10,pady=10)
priceTextBox =  Entry(MidFrame,font=('Helvetica',16),textvariable=price)
priceTextBox.grid(row=6,column=1,padx=10,pady=10)

def add():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'medicine'
    (MedicineName ,MedicineId,Brand ,ChemicalComponent ,MFG_Date ,EXP_Date ,price) values(?,?,?,?,?,?,?)""",
                   (str(medicine_name.get()),str(medicine_id.get()),
                    str(brand.get()),str(chemical_component.get()),
                    str(mfg.get()),str(exp.get()),str(price.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('ADD MEDICINE','New Medicine added',icon='info')


    else:
        msg.showinfo('Error','New Medicine not added',icon='warning')

def back():
    window.destroy()
    import home



add_btn = Button(MidFrame,text='ADD',command=add,
                    font=('Helvetica',18),fg='black',bg='green')
add_btn.grid(row=7,column=1,padx=10,pady=10)





back_btn = Button(MidFrame,text='Back',command=back,
                   font=('Helvetica',18),fg='black',bg='red')
back_btn.grid(row=8,column=1,padx=10,pady=10)




window.mainloop()
