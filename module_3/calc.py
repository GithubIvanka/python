import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    insert_values(num1 + num2)

def sub():
    num1, num2 = get_values()
    insert_values(num1 - num2)

def mul():
    num1, num2 = get_values()
    insert_values(num1 * num2)

def div():
    num1, num2 = get_values()
    insert_values(num1 / num2)


window = tk.Tk()

window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text="+", width=4, height=2, command=add)
button_add.place(x=75, y=175)
button_sub = tk.Button(window, text="-", width=4, height=2, command=sub)
button_sub.place(x=125, y=175)
button_mul = tk.Button(window, text="*", width=4, height=2, command=mul)
button_mul.place(x=175, y=175)
button_div = tk.Button(window, text="/", width=4, height=2, command=div)
button_div.place(x=225, y=175)

number1_entry = tk.Entry(window, width=31)
number1_entry.place(x=75, y=75)
number2_entry = tk.Entry(window, width=31)
number2_entry.place(x=75, y=125)
answer_entry = tk.Entry(window, width=31)
answer_entry.place(x=75, y=275)

number1_text = tk.Label(window, text="Введите первое число:")
number1_text.place(x=75, y=50)
number2_text = tk.Label(window, text="Введите второе число:")
number2_text.place(x=75, y=100)
answer = tk.Label(window, text="Ответ:")
answer.place(x=75, y=250)

window.mainloop()