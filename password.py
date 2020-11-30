from tkinter import *
import mysql.connector
from mysql.connector import Error
from tqdm import tqdm

def db_conn():
	conn = mysql.connector.connect(user='root',database='ridb',host='localhost',password='riddhi1234')
	cursor = conn.cursor()
	return conn,cursor


def window():
	root = Tk()
	file1 = "C:\\Users\\USER\\Desktop\\py1.jpg"
	f = Frame(root,height=115,width=300)
	f.propagate(0)
	f.pack()
	return f,root

def db_insert(idd,nm,pwd):
	string = "INSERT INTO pass(id,name,password) VALUES (%s,%s,%s)"
	values = (idd,nm,pwd)
	con,cur = db_conn()
	cur.execute(string,values)
	con.commit()
	cur.close()
	con.close()
	print("Upload Complete Bro")


def show():

	frame,root= window()
	root.title()
	l = Label(frame,text="User")
	l.pack()
	e1 = Entry(frame)
	e1.pack()
	l2 = Label(frame,text="Password")
	l2.pack()
	e2 = Entry(frame)
	e2.pack()
	enter1=e1.get()
	enter2=e2.get()
	btn = Button(frame,text="correct",height=1,width=10,activebackground="black",activeforeground="white")
	btn.pack(padx=0,pady=5)
	root.mainloop()



show()



