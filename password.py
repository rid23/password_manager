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
	f = Frame(root,height=110,width=300)
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



def click():
	string = "SELECT id FROM pass"
	con,cur = db_conn()
	cur.execute(string)
	#Items from the id column of pass table
	itm=cur.fetchall()
	con.commit()
	cur.close()
	con.close()
	db_insert(int(itm[-1][0])+1,str(e1.get()),str(e2.get()))

frame,win = window()
