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
	f = Frame(root,height=200,width=300)
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

frame,root= window()
root.title()
E = Entry(frame)
E.pack()
btn = Button(frame,text="correct",height=1,width=10,activebackground="black",activeforeground="white")
btn.pack()
root.mainloop()


