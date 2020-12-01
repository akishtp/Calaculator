from tkinter import *

window = Tk()

expression = ""
equation = StringVar()
topEq = StringVar()

photo = PhotoImage(file="calacimg.png")
window.iconphoto(False, photo)

def press(num):
	global expression
	expression+=str(num)
	topEq.set(expression)
	
def pressEquate(equate):
	global expression
	if (expression==""):
		expression=""
	else:
		expression+=str(equate)
	topEq.set(expression)
	
def pressEqual():
	global expression
	total=str(eval(expression))
	mainEq.set(total)
	
def pressSquare():
	global expression
	topEq.set(str('(')+str(expression)+str(")²"))
	expression=str(float(expression)*float(expression))
	mainEq.set(expression)
	
def pressRoot():
	global expression
	topEq.set(str("√")+str(expression))
	expression=str(float(expression)**0.5)
	mainEq.set(expression)
	
def pressInverse():
	global expression
	topEq.set(str("1/")+str("(")+str(expression)+str(")"))
	expression=str(str("1/(")+str(expression)+str(")"))
	
def pressClear():
	global expression
	expression=""
	topEq.set(expression)
	mainEq.set(expression)
	
def pressPercent():
	global expression
	topEq.set(str(expression)+str("%"))
	expression=str("(;´༎ຶД༎ຶ`)")
	mainEq.set(expression)
	
def pressBracket():
	global expression
	topEq.set(str("(")+str(expression)+str(")"))
	expression=str(str("(")+str(expression)+str(")"))
	
def pressMath():
	global expression
	topEq.set("☆Math is Cool☆")
	expression="(♡´౪`♡)"
	mainEq.set(expression)
	expression=""

#UX/UI DESIGN

blankLine = Label(Win,
		bg="Black",
		font=('helvetica',35))
blankLine.grid(row=0,
		columnspan=4)

screenS=Entry(Win,
		width=17,
		border=0,
		font=('helvetica', 20),
		justify=RIGHT,
		textvariable=topEq)
screenS.grid(row=1,
		columnspan=4)
screenB=Entry(width=6,
		border=0,
		font=('helvetica',56),
		justify=RIGHT,
		textvariable=mainEq)
screenB.grid(row=2,
		columnspan=4)
		
buttonBracket= Button(Win,
		text="(  )",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:pressBracket())
buttonBracket.grid(row=3,
		column=0,
		padx=0,
		pady=0)
buttonPercentage= Button(Win,
		text="%",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:pressPercent())
buttonPercentage.grid(row=3,
		column=1,
		padx=0,
		pady=0)
buttonPi=Button(Win,
		text="π",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("3.14"))
buttonPi.grid(row=3,
		column=2,
		padx=0,
		pady=0)
buttonC= Button(Win,
		text="C",
		border=0,
		fg='White',
		bg='#ff4500',
		activebackground='red', 
		height=3, 
		width=6,
		command=lambda:pressClear())
buttonC.grid(row=3,
		column=3,
		padx=0,
		pady=7)

buttonInverse= Button(Win,
		text="1/x",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:pressInverse())
buttonInverse.grid(row=4,
		column=0,
		padx=0,
		pady=0)
buttonSquare= Button(Win,
		text="x²",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:pressSquare())
buttonSquare.grid(row=4,
		column=1,
		padx=0,
		pady=0)
buttonRoot=Button(Win,
		text="√",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:pressRoot())
buttonRoot.grid(row=4,
		column=2,
		padx=0,
		pady=0)
buttonDivide= Button(Win,
		text="÷",
		border=0,
		fg='White',
		bg='#57f281',
		activebackground='#32a852', 
		height=3, 
		width=6,
		command=lambda:pressEquate("/"))
buttonDivide.grid(row=4,
		column=3,
		padx=0,
		pady=7)
		
button7 = Button(Win,
		text="7",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("7"))
button7.grid(row=5,
		column=0,
		padx=0,
		pady=0)
button8= Button(Win,
		text="8",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("8"))
button8.grid(row=5,
		column=1,
		padx=0,
		pady=0)
button9 = Button(Win,
		text="9",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("9"))
button9.grid(row=5,
		column=2,
		padx=0,
		pady=0)
buttonMultiply= Button(Win,
		text="×",
		border=0,
		fg='White',
		bg='#57f281',
		activebackground='#32a852', 
		height=3, 
		width=6,
		command=lambda:pressEquate("*"))
buttonMultiply.grid(row=5,
		column=3,
		padx=0,
		pady=7)
		
button4 = Button(Win,
		text="4",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("4"))
button4.grid(row=6,
		column=0,
		padx=0,
		pady=0)
button5= Button(Win,
		text="5",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("5"))
button5.grid(row=6,
		column=1,
		padx=0,
		pady=0)
button6 = Button(Win,
		text="6",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("6"))
button6.grid(row=6,
		column=2,
		padx=0,
		pady=0)
buttonSubtract= Button(Win,
		text="-",
		border=0,
		fg='White',
		bg='#57f281',
		activebackground='#32a852', 
		height=3, 
		width=6,
		command=lambda:pressEquate("-"))
buttonSubtract.grid(row=6,
		column=3,
		padx=0,
		pady=7)
		
button1= Button(Win,
		text="1",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("1"))
button1.grid(row=7,
		column=0,
		padx=0,
		pady=0)
button2= Button(Win,
		text="2",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("2"))
button2.grid(row=7,
		column=1,
		padx=0,
		pady=0)
button3 = Button(Win,
		text="3",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
	    command=lambda:press("3"))
button3.grid(row=7,
		column=2,
		padx=0,
		pady=0)
buttonAdd= Button(Win,
		text="+",
		border=0,
		fg='White',
		bg='#57f281',
		activebackground='#32a852', 
		height=3, 
		width=6,
		command=lambda:pressEquate("+"))
buttonAdd.grid(row=7,
		column=3,
		padx=0,
		pady=7)
		
buttonMath = Button(Win,
		text="Math",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:pressMath())
buttonMath.grid(row=8,
		column=0,
		padx=0,
		pady=0)
button0= Button(Win,
		text="0",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("0"))
button0.grid(row=8,
		column=1,
		padx=0,
		pady=0)
buttonPoint = Button(Win,
		text="•",
		border=0,
		fg='White',
		bg='#c6c7c8',
		activebackground='#404040', 
		height=3, 
		width=6,
		command=lambda:press("."))
buttonPoint.grid(row=8,
		column=2,
		padx=0,
		pady=0)
buttonEqual= Button(Win,
		text="=",
		border=0,
		fg='white',
		bg='#57f281',
		activebackground='#32a852', 
		height=3, 
		width=6,
		command=pressEqual)
buttonEqual.grid(row=8,
		column=3,
		padx=0,
		pady=7)
Win.mainloop()
