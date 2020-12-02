from tkinter import *
import mysql.connector
from mysql.connector import Error


#storing password in the text file pass.txt
with open("C:\\Users\\USER\\Desktop\\password_manager\\pass.txt") as f:
	pwd = str(f.readline())


def db_conn(pwd):
	#establishing connection eith the mysql
	conn = mysql.connector.connect(user='root',database='ridb',host='localhost',password=pwd)
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
	try:
		string = "INSERT INTO pass(id,name,password) VALUES (%s,%s,%s)"
		values = (idd,nm,pwd)
		con,cur = db_conn()
		cur.execute(string,values)
		con.commit()
		cur.close()
		con.close()
		print("Upload Complete Bro")
	except Exception as e:print(e)


def click(event):
	global enter1,enter2
	# for blank entry in user name and password
	enter1=str(e1.get())
	enter2=str(e2.get())
	if enter1 and enter2 == '':
		fr,root=window()
		print("type in user name or password")	
	elif enter1 =='':
		fr,root=window()
		l1 = Label(fr,text="You left your username blank bro").pack()
	elif enter2 == '':
		fr,root=window()
		l2 = Label(fr,text="enter your password!!!!").pack()
	else:
		print(enter1)
		print(enter2)
		db_insert(idd(),enter1,enter2)



def idd():
	con,cur=db_conn(pwd)
	cur.execute("SELECT id FROM pass")
	itm = cur.fetchall()
	cur.close()
	con.close()
	idd = int(itm[-1][0])+1
	return idd


frame,win = window()

#creating the label,entry,button widgets
label = Label(frame,text="USERNAME")
label2=Label(frame,text="P@$$WORD")
e1=Entry(frame,width=8)
e2=Entry(frame,width=8)
btn=Button(frame,text="Correct",width=6,activebackground="black",activeforeground="white")

#Packing all the widgets
label.pack()
e1.pack()
label2.pack()
e2.pack()
btn.pack()
btn.bind("<Button-1>",click)
win.mainloop()










