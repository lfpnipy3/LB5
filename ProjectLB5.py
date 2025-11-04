
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

# Создаем главное окно приложения
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Создаем кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, command=button_equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda x=button: button_click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Создаем кнопку очистки
tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear).grid(row=5, column=1, columnspan=2)

# Запускаем основной цикл приложения
root.mainloop()