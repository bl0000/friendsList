from tkinter import *
import os.path
import sqlite3
import datetime

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Name')
        self.lbl2=Label(win, text='Scale')
        self.lbl3=Label(win, text='Reason')
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.btn1 = Button(win, text='Enter')
        self.lbl1.place(x=50, y=50)
        self.t1.place(x=150, y=50)
        self.lbl2.place(x=50, y=100)
        self.t2.place(x=150, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b1.place(x=100, y=200)
        self.lbl3.place(x=50, y=150)
        self.t3.place(x=150, y=150)
    def add(self):
        name=str(self.t1.get())
        scale=int(self.t2.get())
        reason=str(self.t3.get())
        db.insertValue(name, scale, reason)

class dbManage():
    def __init__(self):
        self.checkFile = os.path.exists("friendList.db") # create start menu to give user option to create new db or import existing
        self.conn = sqlite3.connect("friendList.db")
        if self.checkFile == True:
            print("Opened database successfully")
        else:
            self.conn.execute('''CREATE TABLE FRIEND_LIST
                             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             NAME           TEXT    NOT NULL,
                             SCALE            INTEGER     NOT NULL,
                             REASONS           CHAR(100)    NOT NULL,
                             DATE           TIMESTAMP    NOT NULL
                             );''')
            print("Table created successfully")

    def insertValue(self,name,scale,reason):
        self.currentDateTime = datetime.datetime.now()
        self.conn.execute('INSERT INTO FRIEND_LIST(NAME, SCALE, REASONS, DATE) VALUES (?,?,?,?)', (name, scale, reason, self.currentDateTime))
        print("Success")
        self.conn.commit()


def close():
    window.destroy()
    db.conn.close()
    print("Closing database")

db = dbManage()
window=Tk()
mywin=MyWindow(window)
window.title('Friend List')
window.geometry("400x320")
window.bind('<Escape>', lambda e: close())
window.mainloop()
