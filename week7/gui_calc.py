from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("150x100")
window.wm_iconbitmap("calc.ico")
ent = Entry(window,width=10,fg="black",bg="white")
ent.place(x=0,y="0")
ent.insert(-1,0)
ans = Label(window, text="",bg="white",fg="black")
ans.place(x=0,y=20)
b = 0
a = int(ent.get())
def add():
	global b
	global a
	b = a+b
	#ans = Label(window,text=f"{b}",bg="white",fg="black")
	#ans.place(x=0,y=20)
	ans.configure(text=f"{b}")
def multi():
	global b
	global a
	b = a*b
	#ans = Label(window,text=f"{b}",bg="white",fg="black")
	#ans.place(x=0,y=20)
	ans.configure(text=f"{b}")
def div():
	global b
	global a
	b = b/a
	#ans = Label(window,text=f"{b}",bg="white",fg="black")
	#ans.place(x=0,y=20)
	ans.configure(text=f"{b}")
def sub():
	global b
	global a
	b = b-a
	#ans = Label(window,text=f"{b}",bg="white",fg="black")
	#ans.place(x=0,y=20)
	ans.configure(text=f"{b}")

bt1 = Button(window,text=" +",bg="black",fg="white",command=add)
bt1.place(x=0,y=40)
bt2 = Button(window,text=" - ",bg="black",fg="white",command=sub)
bt2.place(x=25,y=40)
bt3 = Button(window,text=" * ",bg="black",fg="white",command=multi)
bt3.place(x=0,y=70)
bt4 = Button(window,text=" / ",bg="black",fg="white",command=div)
bt4.place(x=25,y=70)
	
window.mainloop()