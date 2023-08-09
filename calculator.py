#-----------------------CODSOFT (INTERNSHIP ..... PYTHON PROGRAMMING)-------------------------------------

# NAME - SMRITI SAROJ SINHA
# COLLEGE - CENTRAL UNIVERSITY OF HARYANA

#------------------------------CALCULATOR --------------------------------

# importing from tkinter module
from tkinter import *
import tkinter.font as font 
# global variable
ex = ""  #VARIABLE FOR EXPRESSION

# Function to take the expression from tne user in the calculator
# the text box 
def press(num):
	global ex
	ex = ex + str(num)
	equation.set(ex)

# Function to evaluate the final expression
def equalpress():
	# using Try and except statement for handling the errors like zero division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:
		global ex

		# evaluating the function using eval function and convert the result into string using str functiom
		total = str(eval(ex))
		equation.set(total)

		# initialising the expression by the empty string
		ex = ""

	# for handling the error if generated
	except:
		equation.set(" error ")
		ex = ""


# Function to clear the contents of text entry box
def clear():
	global ex
	ex = ""
	equation.set("")

#Function to clear the last digit of the expression in the entry box
def clearlastchar(self , event = None):
	current = self.text.box.get()[:-1]
	self.text.box.delete(0,END)
	self.text.box.current(INSERT , Text)
	
# Driver code
if __name__ == "__main__":
	
	gui = Tk() #GUI window
	gui.configure(background="lavender") #background color
	gui.title("Simple Calculator") #title of the calculator
	gui.geometry("280x340") #configuration of the window
	equation = StringVar() #the variable class
	ex_field = Entry(gui, textvariable=equation , bd=3 , relief=SUNKEN , width=40 ) #creating the text box for displaying and typing the expression
	
	#grid method is used for placing the widgets at respective position in table like structure
	ex_field.grid(columnspan=5, padx=13, ipadx = 5 , pady= 4 )
	
	# creating the buttons
	button1 = Button(gui, text=' 1 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(1), height=3, width=8)
	button1.grid(row=4, column=0 , pady = 5)

	button2 = Button(gui, text=' 2 ', fg='black', bg='DarkSlateGray3' ,
					command=lambda: press(2), height=3, width=8)
	button2.grid(row=4, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(3), height=3, width=8)
	button3.grid(row=4, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(4), height=3, width=8)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(5), height=3, width=8)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(6), height=3, width=8)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(7), height=3, width=8)
	button7.grid(row=2, column=0 , pady = 5)

	button8 = Button(gui, text=' 8 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(8), height=3, width=8)
	button8.grid(row=2, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(9), height=3, width=8)
	button9.grid(row=2, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='DarkSlateGray3',
					command=lambda: press(0), height=3, width=8)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='LightGoldenrod1',
				command=lambda: press("+"), height=3, width=8)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='LightGoldenrod1',
				command=lambda: press("-"), height=3, width=8)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='LightGoldenrod1',
					command=lambda: press("*"), height=3, width=8)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='LightGoldenrod1',
					command=lambda: ("/"), height=3, width=8)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='LightGoldenrod1',
				command=equalpress, height=3, width=8)
	equal.grid(row=6, column=3)

	rbracket = Button(gui, text=' ( ', fg='black', bg='LightGoldenrod1',
					command=lambda: press("("), height=3, width=8)
	rbracket.grid(row=6, column=1)

	lbracket = Button(gui, text=' ) ', fg='black', bg='LightGoldenrod1',
					command=lambda: press(")"), height=3, width=8)
	lbracket.grid(row=6, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='LightGoldenrod1',
				command=clear, height=3, width=8)
	clear.grid(row=6, column=0 , pady = 5)
	
	clearlastchar = Button(gui, text='←', fg='black', bg='LightGoldenrod1',
				command=clearlastchar, height=3, width=8)
	clearlastchar.grid(row=5, column=2 )

	Decimal= Button(gui, text='.', fg='black', bg='LightGoldenrod1',
					command=lambda: press('.'), height=3, width=8)
	Decimal.grid(row=5, column=1)
	
	gui.mainloop()
