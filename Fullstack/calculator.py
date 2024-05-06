from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=43, borderwidth=8, bg="grey", fg="black")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=15)



def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0, END)    

def add():
    num1 = e.get()
    global f_num
    global maths
    maths = "addition"
    f_num = int(num1)
    e.delete(0, END)

def equal_to():
    num2 = e.get()
    e.delete(0, END)
    
    if maths == "addition":
        e.insert(0, f_num + int(num2))
    
    elif maths == "subtraction":
        e.insert(0, f_num - int(num2))
    
    elif maths == "multiplication":
        e.insert(0, f_num * int(num2))
    
    elif maths == "division":
        e.insert(0, f_num / int(num2))

    else:
        e.insert(0, "ERROR")   

def subtract():
    num1 = e.get()
    global f_num
    global maths
    maths = "subtraction"
    f_num = int(num1)
    e.delete(0, END)

def multiply():
    num1 = e.get()
    global f_num
    global maths
    maths = "multiplication"
    f_num = int(num1)
    e.delete(0, END)

def divide():
    num1 = e.get()
    global f_num
    global maths
    maths = "division"
    f_num = int(num1)
    e.delete(0, END)


#define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: add())
button_equal_to = Button(root, text="=", padx=86, pady=20, command=lambda: equal_to())
button_clear = Button(root, text="Clear", padx=76, pady=20, command=lambda: clear())

button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: subtract())
button_multiply = Button(root, text="x", padx=41, pady=20, command=lambda: multiply())
button_divide = Button(root, text="/", padx=39, pady=20, command=lambda: divide())
#print on the srceen

button_1.grid(row=3, column=2, padx=1, pady=1)
button_2.grid(row=3, column=1, padx=1, pady=1)
button_3.grid(row=3, column=0, padx=1, pady=1)
button_4.grid(row=2, column=2, padx=1, pady=1)
button_5.grid(row=2, column=1, padx=1, pady=1)
button_6.grid(row=2, column=0, padx=1, pady=1)
button_7.grid(row=1, column=2, padx=1, pady=1)
button_8.grid(row=1, column=1, padx=1, pady=1)
button_9.grid(row=1, column=0, padx=1, pady=1)
button_0.grid(row=4, column=0, padx=1, pady=1)
button_add.grid(row=5, column=0, padx=1, pady=1)
button_equal_to.grid(row=5, column=1, padx=1, pady=1, columnspan=3)
button_clear.grid(row=4, column=1, padx=1, pady=1, columnspan=2)

button_subtract.grid(row=6, column=0, padx=1, pady=1)
button_multiply.grid(row=6, column=1, padx=1, pady=1)
button_divide.grid(row=6, column=2, padx=1, pady=1)

root.mainloop()