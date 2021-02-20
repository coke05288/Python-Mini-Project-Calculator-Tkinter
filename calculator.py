from tkinter import *
from tkinter import ttk

# 함수
def button_pressed(value):
    number_entry.insert("end", value)
    print(value, "pressed")

def math_button_pressed(value):
    print(value,"pressed")
     
def equal_button_pressed():
    print("equal pressed")

root = Tk()
root.title("Calculator")
root.geometry("300x200")

# 숫자 기입 표시창
number_entry = ttk.Entry(root, width=20)
number_entry.grid(row=0, columnspan=3)

# 숫자 버튼
div_button = ttk.Button(root, text="/", command=lambda:math_button_pressed("/"))
div_button.grid(row=1, column=0)
multi_button = ttk.Button(root, text="*", command=lambda:math_button_pressed("*"))
multi_button.grid(row=1, column=1)
sub_button = ttk.Button(root, text="-", command=lambda:math_button_pressed("-"))
sub_button.grid(row=1, column=2)

number_button7 = ttk.Button(root, text="7", command=lambda:button_pressed("7"))
number_button7.grid(row=2, column=0)
number_button8 = ttk.Button(root, text="8", command=lambda:button_pressed("8"))
number_button8.grid(row=2, column=1)
number_button9 = ttk.Button(root, text="9", command=lambda:button_pressed("9"))
number_button9.grid(row=2, column=2)

number_button4 = ttk.Button(root, text="4", command=lambda:button_pressed("4"))
number_button4.grid(row=3, column=0)
number_button5 = ttk.Button(root, text="5", command=lambda:button_pressed("5"))
number_button5.grid(row=3, column=1)
number_button6 = ttk.Button(root, text="6", command=lambda:button_pressed("6"))
number_button6.grid(row=3, column=2)

number_button1 = ttk.Button(root, text="1", command=lambda:button_pressed("1"))
number_button1.grid(row=4, column=0)
number_button2 = ttk.Button(root, text="2", command=lambda:button_pressed("2"))
number_button2.grid(row=4, column=1)
number_button3 = ttk.Button(root, text="3", command=lambda:button_pressed("3"))
number_button3.grid(row=4, column=2)

dot_button = ttk.Button(root, text=".", command=lambda:button_pressed("."))
dot_button.grid(row=5, column=0)
number_button0 = ttk.Button(root, text="0", command=lambda:button_pressed("0"))
number_button0.grid(row=5, column=1)
equal_button = ttk.Button(root, text="=", command=lambda:equal_button_pressed())
equal_button.grid(row=5, column=2)

root.mainloop()
