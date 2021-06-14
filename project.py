from tkinter import *
from tkinter import messagebox
import os
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="ashwin6cs01!",db="srm")
mycursor = db.cursor()

w = Tk()
w.geometry('350x500')
w.title(' L O G I N ')
w.resizable(0, 0)

j = 0
r = 10
for i in range(100):
    c = str(222222 + r)
    Frame(w, width=10, height=500, bg="#" + c).place(x=j, y=0)
    j = j + 10
    r = r + 1

Frame(w, width=250, height=400, bg='white').place(x=50, y=50)

l1 = Label(w, text='Username', bg='white')
z1 = ('Consolas', 13)
l1.config(font=z1)
l1.place(x=80, y=215)

e1 = Entry(w, width=20, border=0)
z2 = ('Consolas', 13)
e1.config(font=z2)
e1.place(x=80, y=248)


e2 = Entry(w, width=20, border=0, show='*')
e2.config(font=z2)
e2.place(x=80, y=322)

l2 = Label(w, text='Password', bg='white')
l = ('Consolas', 13)
l2.config(font=l)
l2.place(x=80, y=285)



Frame(w, width=180, height=2, bg='#141414').place(x=80, y=342)
Frame(w, width=180, height=2, bg='#141414').place(x=80, y=270)

from PIL import ImageTk, Image

n1 = Image.open("log.png")
n2 = ImageTk.PhotoImage(n1)

labe1 = Label(image=n2 , border=0 , justify=CENTER)

labe1.place(x=109, y=54)


def cmd():
    if e1.get() == 'ashwin' and e2.get() == 'ashwin6cs01!':
        messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
        root = Tk()
        root.title("Pharmacy Managment System")
        root.configure(width=1500, height=600, bg='#160161')
        

        def additem():
            e1 = entry1.get()
            e2 = entry2.get()
            e3 = entry3.get()
            e4 = entry4.get()
            e5 = entry5.get()
            sql = "INSERT INTO pharmacy (item_name, item_price, item_quantity, item_category, item_discount) VALUES (%s, %s, %s, %s, %s)"
            val = (str(e1),float(e2),int(e3),str(e4),int(e5))
            mycursor.execute(sql, val)
            db.commit()
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

        def deleteitem():
            e1 = entry1.get()
            sql = "DELETE FROM pharmacy WHERE item_name=%s;"
            adr = (str(e1),)
            mycursor.execute(sql, adr)
            db.commit()
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

        def firstitem():
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            mycursor.execute("SELECT * FROM pharmacy ORDER BY item_name LIMIT 1;")
            result = mycursor.fetchall()
            entry1.insert(0, result[0][0])
            entry2.insert(0, result[0][1])
            entry3.insert(0, result[0][2])
            entry4.insert(0, result[0][3])
            entry5.insert(0, result[0][4])

        def nextitem():
            try:
                e1 = entry1.get()
                e2 = entry2.get()
                e3 = entry3.get()
                e4 = entry4.get()
                e5 = entry5.get()
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                sql = "SELECT * FROM pharmacy WHERE item_name >%s ORDER BY  item_name LIMIT 1;"
                adr = (e1,)
                mycursor.execute(sql, adr)
                result = mycursor.fetchall()
                entry1.insert(0, str(result[0][0]))
                entry2.insert(0, str(result[0][1]))
                entry3.insert(0, str(result[0][2]))
                entry4.insert(0, str(result[0][3]))
                entry5.insert(0, str(result[0][4]))
            except:
                messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

        def previousitem():
            try:
               
                e1 = entry1.get()
                e2 = entry2.get()
                e3 = entry3.get()
                e4 = entry4.get()
                e5 = entry5.get()
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                sql = "SELECT * FROM pharmacy WHERE item_name <%s ORDER BY  item_name DESC LIMIT 1;"
                adr = (e1,)
                mycursor.execute(sql, adr)
                result = mycursor.fetchall()
                entry1.insert(0, str(result[0][0]))
                entry2.insert(0, str(result[0][1]))
                entry3.insert(0, str(result[0][2]))
                entry4.insert(0, str(result[0][3]))
                entry5.insert(0, str(result[0][4]))
            except:
                messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

        def lastitem():
            try:
                
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                mycursor.execute("SELECT * FROM pharmacy ORDER BY item_name DESC LIMIT 1;")
                result = mycursor.fetchall()

                entry1.insert(0, result[0][0])
                entry2.insert(0, result[0][1])
                entry3.insert(0, result[0][2])
                entry4.insert(0, result[0][3])
                entry5.insert(0, result[0][4])
            except:
                messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

        def updateitem():

            e1 = entry1.get()
            e2 = entry2.get()
            e3 = entry3.get()
            e4 = entry4.get()
            e5 = entry5.get()
            sql = "UPDATE pharmacy SET item_name = %s,item_price = %s,item_quantity = %s,item_category = %s,item_discount = %s WHERE item_name = %s"
            val = (str(e1),e2,e3,str(e4),e5,str(e1))
            mycursor.execute(sql, val)
            db.commit()

        def clearitem():
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

        label0 = Label(root, text="PHARMACY MANAGEMENT SYSTEM ", bg="black", fg="#f7fc68", font=("Times", 30))
        label1 = Label(root, text="ENTER ITEM NAME", bg="red", relief="ridge", fg="black", font=("Times", 12, 'bold'), width=25)
        entry1 = Entry(root, font=("Times", 12, 'bold'))
        label2 = Label(root, text="ENTER ITEM PRICE", bd="2", relief="ridge", height="1", bg="red", fg="black",
                       font=("Times", 12, 'bold'), width=25)
        entry2 = Entry(root, font=("Times", 12, 'bold'))
        label3 = Label(root, text="ENTER ITEM QUANTITY", bd="2", relief="ridge", bg="red", fg="black",
                       font=("Times", 12, 'bold'), width=25)
        entry3 = Entry(root, font=("Times", 12, 'bold'))
        label4 = Label(root, text="ENTER ITEM CATEGORY", bd="2", relief="ridge", bg="red", fg="black",
                       font=("Times", 12, 'bold'), width=25)
        entry4 = Entry(root, font=("Times", 12, 'bold'))
        label5 = Label(root, text="ENTER ITEM DISCOUNT", bg="red", relief="ridge", fg="black", font=("Times", 12, 'bold'),
                       width=25)
        entry5 = Entry(root, font=("Times", 12, 'bold'))
        button1 = Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'), command=additem)
        button2 = Button(root, text="DELETE ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=deleteitem)
        button3 = Button(root, text="VIEW FIRST ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=firstitem)
        button4 = Button(root, text="VIEW NEXT ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=nextitem)
        button5 = Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=previousitem)
        button6 = Button(root, text="VIEW LAST ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=lastitem)
        button7 = Button(root, text="UPDATE ITEM", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=updateitem)
        button9 = Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12, 'bold'),
                         command=clearitem)
        label0.grid(columnspan=6, padx=10, pady=10)
        label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
        label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
        entry1.grid(row=1, column=1, padx=40, pady=10)
        entry2.grid(row=2, column=1, padx=10, pady=10)
        entry3.grid(row=3, column=1, padx=10, pady=10)
        entry4.grid(row=4, column=1, padx=10, pady=10)
        entry5.grid(row=5, column=1, padx=10, pady=10)
        button1.grid(row=1, column=4, padx=40, pady=10)
        button2.grid(row=1, column=5, padx=40, pady=10)
        button3.grid(row=2, column=4, padx=40, pady=10)
        button4.grid(row=2, column=5, padx=40, pady=10)
        button5.grid(row=3, column=4, padx=40, pady=10)
        button6.grid(row=3, column=5, padx=40, pady=10)
        button7.grid(row=4, column=4, padx=40, pady=10)
        button9.grid(row=4, column=5, padx=40, pady=10)
        root.mainloop()
    else:
        messagebox.showwarning("LOGIN FAILED", "        PLEASE TRY AGAIN        ")


def bttn(x, y, text, ecolor, lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor  
        myButton1['foreground'] = lcolor  

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground'] = ecolor

    myButton1 = Button(w, text=text,
                       width=20,
                       height=2,
                       fg=ecolor,
                       border=0,
                       bg=lcolor,
                       activeforeground=lcolor,
                       activebackground=ecolor,
                       command=cmd)

    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x, y=y)


bttn(100, 375, 'L O G I N', 'white', '#994422')

w.mainloop()

