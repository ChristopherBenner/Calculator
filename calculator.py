#Calculator.py
#Author Christopher Benner
#Date Created 2 Jan 2023
#Python version 3.11.0
#This is a fully functional 4 function calculator which allows for multiple arguments before hitting enter
#Most other simple calculator apps require you to insert the first number followed by the operation
#followed by the second number and finally the equals sign. Straying from this format makes the calculator lose functionality
#This calculator instead keeps a running total ex inputting 2 + 2 would automatically output 4 if another operation is selected
#This way you can keep going without having to hit equals every time. Additionally, there is the option to continue the problem
#after selecting enter. 

total = 0
last_operation = 'clear'
new_number = 0 
last_number = 0
equal_clicked = False
add_number = False
error = False
zero_clicked = False

from tkinter import *

root = Tk()
root.title("Simple Calculator")
Font_tuple = ("Helvetica", 14)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column = 0, columnspan =3,padx = 10, pady = 10)

def button_click(number):
	global last_operation, last_number, equal_clicked, add_number, error,zero_clicked
	
	if equal_clicked or not add_number or error:
		#Check to see if an operation or error has occurred since the last number was inserted
		e.delete(0,END)
		add_number = True
		error = False
		equal_clicked = False
		
	current = e.get()

	if '.' in current and number == '.':
		#prevent the possibility of having two decimals in the same number
		return
	if len(current) == 0 and number == '.':
		#Ensure there is a leading zero if the decimal is clicked and nothing else 
		e.insert(0,'0.')
	elif number == 'change':
		if len(current) != 0:
			e.delete(0,END)
			e.insert(0, float(current) * -1)
	else:
		e.insert(len(current),number)
	zero_remove(zero_clicked)
	if number == 0:
		zero_clicked = True
	else:
		zero_clicked = False
	try:	
		last_number = float(e.get())
	except:
		return

def zero_remove(zero_clicked):
	current = e.get()
	try:
		if current[-2:] == '.0' and not zero_clicked:
			no_zero = current[:-2]
			e.delete(0,END)
			e.insert(0,no_zero)
	except IndexError:
		return
		



def clear():
	global total, last_operation, last_number, add_number, equal_clicked,error
	if not error:
		e.delete(0,END)
	total = 0
	last_operation = 'clear'
	last_number = 0
	add_number = False
	equal_clicked = False

def button_equal(operation):
	global last_operation, equal_clicked, total, add_number, error, zero_clicked
	try:
		first_number = float(e.get())
	except:
		return
	e.delete(0,END)

	if last_operation == 'clear' or last_operation == 'equals':
		total = first_number
	if last_operation == 'plus' and not equal_clicked :
		total += last_number
		e.insert(0,total)
	if last_operation == 'subtract' and not equal_clicked:
		total -= last_number
		e.insert(0,total)
	if last_operation == 'multiply' and not equal_clicked:
		total *= last_number
		e.insert(0,total)
	if last_operation == 'divide' and not equal_clicked:
		if last_number != 0:
			total /= last_number
			e.insert(0,total)
		else:
			e.insert(0,"ERR: DIVIDE BY ZERO")
			error = True
			clear()
			return
	last_operation = operation
	if operation == 'equals':
		e.delete(0,END)
		e.insert(0,total)
		equal_clicked  = True
	else:
		equal_clicked = False
	add_number = False
	zero_clicked = False
	zero_remove(zero_clicked)
#Define the buttons
button_1 =Button(root,text="1",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(1))
button_2 =Button(root,text="2",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(2))
button_3 =Button(root,text="3",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(3))
button_4 =Button(root,text="4",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(4))
button_5 =Button(root,text="5",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(5))
button_6 =Button(root,text="6",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(6))
button_7 =Button(root,text="7",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(7))
button_8 =Button(root,text="8",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(8))
button_9 =Button(root,text="9",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(9))
button_0 =Button(root,text="0",padx = 40, pady=20,activebackground = 'light gray',command=lambda: button_click(0))

button_equals = Button(root,text="=",padx=86,pady=20,activebackground = 'light gray',command=lambda:button_equal('equals'))
button_clear = Button(root,text="Clear",padx =77, pady=20,activebackground = 'light gray',command=clear)

button_plus = Button(root,text="+",padx = 38, pady=20,activebackground = 'light gray',command=lambda: button_equal('plus'))
button_subtract = Button(root,text="-",padx = 39, pady=20,activebackground = 'light gray',command=lambda: button_equal('subtract'))
button_multiply = Button(root,text="*",padx = 39, pady=20,activebackground = 'light gray',command=lambda: button_equal('multiply'))
button_divide = Button(root,text="/",padx = 39, pady=20,activebackground = 'light gray',command=lambda: button_equal('divide'))
button_decimal = Button(root,text=".", font= Font_tuple, padx = 37, pady=14, activebackground = 'light gray',command=lambda: button_click('.'))
button_change = Button(root,text="+/-", padx = 34, pady=20, activebackground = 'light gray',command=lambda: button_click('change'))

#put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_equals.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5,column=0,columnspan=2)
button_change.grid(row=5,column=2)

button_decimal.grid(row=5, column=3)
button_plus.grid(row=4,column=3)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=1,column=3)

root.mainloop()