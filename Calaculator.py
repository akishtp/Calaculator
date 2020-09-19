from tkinter import *

window = Tk()

expression = ""
equation = StringVar()
topEq = StringVar()

photo = PhotoImage(file="calacimg.png")
window.iconphoto(False, photo)


def press(num):
    global expression
    global topEq
    expression = expression + str(num)
    equation.set(expression)
    topEq.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")
    topEq.set(expression)


def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)


def squarepress():
    global expression
    global topEq
    topEq.set(str('(') + str(expression) + str(')²'))
    expression = str(int(expression) * int(expression))
    equation.set(expression)


def rootpress():
    global expression
    global topEq
    topEq.set('√' + str(expression))
    expression = str(int(expression) ** 0.5)
    equation.set(expression)


window.title('Calaculator')
window.geometry("544x570")
window.configure(highlightbackground='white')

screen2 = Entry(window, width=36, border=0, font=('helvetica', 20), justify=RIGHT, cursor='arrow', textvariable=topEq)
screen1 = Entry(window, width=12, font=('helvetica', 60), border=0, justify=RIGHT, textvariable=equation)
buttonC = Button(window, text="C", border=0, fg='red', bg='#9e9e9e', activebackground='red', height=4, width=11, font=0, command=clear)
buttonSquare = Button(window, text="x²", border=0, fg='white', bg='#9e9e9e', height=4, width=11, font=0,
                      command=squarepress)
buttonRoot = Button(window, text="√", border=0, fg='white', bg='#9e9e9e'
                                                               '', height=4, width=11, font=0, command=rootpress)
buttonDivide = Button(window, text="÷", border=0, fg='white', activebackground='#00fa4f', bg='#41e876', height=4, width=11, font=0,
                      command=lambda: press("/"))
button7 = Button(window, text="7", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(7))
button8 = Button(window, text="8", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(8))
button9 = Button(window, text="9", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(9))
buttonMultiply = Button(window, text="x", border=0, fg='white', activebackground='#00fa4f', bg='#41e876', height=4, width=11, font=0,
                        command=lambda: press("*"))
button4 = Button(window, text="4", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(4))
button5 = Button(window, text="5", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(5))
button6 = Button(window, text="6", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(6))
buttonSubtract = Button(window, text="-", border=0, fg='white', activebackground='#00fa4f', bg='#41e876', height=4, width=11, font=0,
                        command=lambda: press("-"))
button1 = Button(window, text="1", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(1))
button2 = Button(window, text="2", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(2))
button3 = Button(window, text="3", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(3))
buttonAdd = Button(window, text="+", border=0, fg='white', activebackground='#00fa4f', bg='#41e876', height=4, width=11, font=0,
                   command=lambda: press("+"))
button00 = Button(window, text="00", border=0, fg='black', bg='white', height=4, width=11, font=0,
                  command=lambda: press('00'))
button0 = Button(window, text="0", border=0, fg='black', bg='white', height=4, width=11, font=0,
                 command=lambda: press(0))
buttonPoint = Button(window, text=".", border=0, fg='black', bg='white', height=4, width=11, font=0,
                     command=lambda: press('.'))
buttonEqual = Button(window, text="=", border=0, fg='white', bg='#308546', height=4,
                     width=11, font=0, command=equalpress)

screen2.grid(row=0, padx=0, pady=0, columnspan=4)
screen1.grid(row=1, padx=0, pady=0, columnspan=4)
buttonC.grid(row=2, column="0", padx=0, pady=0)
buttonSquare.grid(row=2, column="1", padx=0, pady=0)
buttonRoot.grid(row=2, column="2", padx=0, pady=0)
buttonDivide.grid(row=2, column="3", padx=0, pady=0)
button7.grid(row=3, column="0", padx=0, pady=0)
button8.grid(row=3, column="1", padx=0, pady=0)
button9.grid(row=3, column="2", padx=0, pady=0)
buttonMultiply.grid(row=3, column="3", padx=0, pady=0)
button4.grid(row=4, column="0", padx=0, pady=0)
button5.grid(row=4, column="1", padx=0, pady=0)
button6.grid(row=4, column="2", padx=0, pady=0)
buttonSubtract.grid(row=4, column="3", padx=0, pady=0)
button1.grid(row=5, column="0", padx=0, pady=0)
button2.grid(row=5, column="1", padx=0, pady=0)
button3.grid(row=5, column="2", padx=0, pady=0)
buttonAdd.grid(row=5, column="3", padx=0, pady=0)
button00.grid(row=6, column="0", padx=0, pady=0)
button0.grid(row=6, column="1", padx=0, pady=0)
buttonPoint.grid(row=6, column="2", padx=0, pady=0)
buttonEqual.grid(row=6, column="3", padx=0, pady=0)

window.mainloop()
