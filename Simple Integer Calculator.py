""" By following Tkinter Course - Create Graphic User interfaces in Python Tutorial
by Codemy.com I have made a simple calculator which calculates two integers.
However I encountered the ZeroDivisionError and
I have added a fix at line 45 which catches and shows the error to the user.
I also added for each calculus button a ValueError catch, in case the user inputs are not integers.
Following this course I am learning to create GUIs in Python using Tkinter library. """

from tkinter import *

# Setting up the window and it's appearance
window = Tk()
window.title("Only Integers Calculator")
window.configure(bg="gray")

# Setting up the input - output box
input_output_box = Entry(window, width=35, borderwidth=5, bg="#e0e0e0")
input_output_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function that displays the numbers or multiple digit numbers accordingly when inputting them
def button_click(number):
    current = input_output_box.get()
    input_output_box.delete(0, END)
    input_output_box.insert(0, str(current) + str(number))


# The delete attribute for the Clear button
def button_clears():
    input_output_box.delete(0, END)


# Calculus output, depending on the "result" variable
def button_equals():
    second_number = input_output_box.get()
    input_output_box.delete(0, END)

    if result == "add":
        try:
            input_output_box.insert(0, f_num + int(second_number))
        except ValueError:
            input_output_box.insert(0, "Invalid input, try integers")
    elif result == "subtract":
        try:
            input_output_box.insert(0, f_num - int(second_number))
        except ValueError:
            input_output_box.insert(0, "Invalid input, try integers")
    elif result == "multiply":
        try:
            input_output_box.insert(0, f_num * int(second_number))
        except ValueError:
            input_output_box.insert(0, "Invalid input, try integers")
    elif result == "divide":
        # Catching the DivideByZero error and displaying it to the user
        try:
            input_output_box.delete(0, END)
            input_output_box.insert(0, f_num // int(second_number))
        except ZeroDivisionError:
            input_output_box.insert(0, "ZeroDivisionError: integer division by zero")


# functions for each calculus sign
# where the global variable "result" differs depending on which sign is clicked
def button_adds():
    try:
        first_number = input_output_box.get()
        global f_num
        global result
        result = "add"
        f_num = int(first_number)
        input_output_box.delete(0, END)
    except ValueError:
        input_output_box.delete(0, END)
        input_output_box.insert(0, "Invalid input, try integers")


def button_subtracts():
    try:
        first_number = input_output_box.get()
        global f_num
        global result
        result = "subtract"
        f_num = int(first_number)
        input_output_box.delete(0, END)
    except ValueError:
        input_output_box.delete(0, END)
        input_output_box.insert(0, "Invalid input, try integers")


def button_multiplies():
    try:
        first_number = input_output_box.get()
        global f_num
        global result
        result = "multiply"
        f_num = int(first_number)
        input_output_box.delete(0, END)
    except ValueError:
        input_output_box.delete(0, END)
        input_output_box.insert(0, "Invalid input, try integers")


def button_divides():
    try:
        first_number = input_output_box.get()
        global f_num
        global result
        result = "divide"
        f_num = int(first_number)
        input_output_box.delete(0, END)
    except ValueError:
        input_output_box.delete(0, END)
        input_output_box.insert(0, "Invalid input, try integers")


# The appearance and the numbers attributed or function for each button
button_1 = Button(window, text="1", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(3))

button_4 = Button(window, text="4", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(6))

button_7 = Button(window, text="7", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(9))

button_0 = Button(window, text="0", padx=40, pady=20, highlightbackground="orange", command=lambda: button_click(0))
button_clear = Button(window, text="C", padx=40, pady=20, highlightbackground="#FFDAB9", command=button_clears)

button_addition = Button(window, text="+", padx=38, pady=20, highlightbackground="#AFEEEE", command=button_adds)
button_subtract = Button(window, text="-", padx=38, pady=20, highlightbackground="#AFEEEE", command=button_subtracts)
button_divide = Button(window, text="÷", padx=38, pady=20, highlightbackground="#AFEEEE", command=button_divides)
button_multiply = Button(window, text="x", padx=38, pady=20, highlightbackground="#AFEEEE", command=button_multiplies)
button_equal = Button(window, text="=", padx=40, pady=20, highlightbackground="#48D1CC", command=button_equals)

# positioning the buttons on the screen by using the grid system
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)

button_addition.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_divide.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_equal.grid(row=4, column=2)

# infinite loop which makes the calculator run constantly
window.mainloop()