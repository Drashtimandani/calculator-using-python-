from tkinter import *

window = Tk()
window.title('Simple Calculator')

e = Entry(window, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#for displaying the entered number
def btn_click(number):
    num = e.get()
    e.delete(0,END)
    e.insert(0, str(num)+str(number))

def btn_add():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num=int(first_num)
    e.delete(0,END)

def btn_sub():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0, END)

def btn_mul():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0, END)

def btn_div():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0, END)

def btn_clr():
    e.delete(0,END)

def btn_eql():
    second_number = e.get()
    e.delete(0,END)

    if math == 'addition':
        e.insert(0,f_num + int(second_number))

    if math == 'subtraction':
        e.insert(0,f_num - int(second_number))

    if math == 'multiplication':
        e.insert(0,f_num * int(second_number))

    if math == 'division':
        e.insert(0,f_num / int(second_number))


#defining buttons

button_0 = Button(window, text='0', padx=30, pady=25, command=lambda: btn_click(0))
button_1 = Button(window, text='1', padx=30, pady=25, command=lambda: btn_click(1))
button_2 = Button(window, text='2', padx=30, pady=25, command=lambda: btn_click(2))
button_3 = Button(window, text='3', padx=30, pady=25, command=lambda: btn_click(3))
button_4 = Button(window, text='4', padx=30, pady=25, command=lambda: btn_click(4))
button_5 = Button(window, text='5', padx=30, pady=25, command=lambda: btn_click(5))
button_6 = Button(window, text='6', padx=30, pady=25, command=lambda: btn_click(6))
button_7 = Button(window, text='7', padx=30, pady=25, command=lambda: btn_click(7))
button_8 = Button(window, text='8', padx=30, pady=25, command=lambda: btn_click(8))
button_9 = Button(window, text='9', padx=30, pady=25, command=lambda: btn_click(9))
button_add = Button(window, text='+', padx=28, pady=25, command=btn_add)
button_sub = Button(window, text='-', padx=30, pady=25, command=btn_sub)
button_mul = Button(window, text='*', padx=30, pady=25, command=btn_mul)
button_div = Button(window, text='/', padx=30, pady=25, command=btn_div)
button_clear = Button(window, text='Clear', padx=19, pady=25, command=btn_clr)
button_eql = Button(window, text='=', padx=30, pady=25, command=btn_eql)

#placing buttons

button_0.grid(row=4, column=1)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_clear.grid(row=4, column=0)
button_eql.grid(row=4, column=2)

window.mainloop()