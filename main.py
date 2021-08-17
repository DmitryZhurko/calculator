import tkinter
from tkinter import messagebox
# Функция вывода в строку цифр
def digit(a):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tkinter.END)
    value = value + str(a)
    calc.insert(0,value)
# Функция подсчета результатов
def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc.delete(0,tkinter.END)
    try:
        calc.insert(0, eval(value))
    except (NameError,SyntaxError):
        messagebox.showinfo('Ошибка', 'Нужно вводить только цифры!')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка', 'Нельзя делить на ноль, пора бы это уже запонить!')
        calc.insert(0, 0)

# Функция ввода в строку операций
def make_operation(opertion):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tkinter.END)
    calc.insert(0, value + opertion)
# Функция очистики строки ввода
def clear_result():
    calc.delete(0, tkinter.END)
    calc.insert(0, '0')
# Функция обработки событий на клавиатуру
def press_key(event):
    if event.char.isdigit():
        digit(event.char)
    elif event.char in '+-*/':
        make_operation(event.char)
    elif event.char == '\r':
        calculate()

# Создаем окно калькулятора
windows = tkinter.Tk()
windows.title('калькулятор')
# Задаем цвет фона
windows['bg'] = '#a551a7'
# Устанавливаем размер окна
windows.geometry('300x400+100+200')
# Устанавливаем фото калькулятора
photo = tkinter.PhotoImage(file='TeachMeSkills.png')
windows.iconphoto(False, photo)
# Устанавливаем обработчик событий на клавиатуру
windows.bind('<Key>', press_key)
# Создаем поле для ввода информации
calc = tkinter.Entry(windows, justify=tkinter.RIGHT, font=('Ink Free',15,'bold'),width=15)
calc.insert(0,0)
calc.grid(row=0, column=0, columnspan=4, stick='wesn')
# Создаем кнопки калькулятора
button_7 = tkinter.Button(windows, text=7, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(7)).grid(row=1, column=0, stick='wesn')
button_8 = tkinter.Button(windows, text=8, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(8)).grid(row=1, column=1, stick='wesn')
button_9 = tkinter.Button(windows, text=9, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(9)).grid(row=1, column=2, stick='wesn')
button_4 = tkinter.Button(windows, text=4, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(4)).grid(row=2, column=0, stick='wesn')
button_5 = tkinter.Button(windows, text=5, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(5)).grid(row=2, column=1, stick='wesn')
button_6 = tkinter.Button(windows, text=6, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(6)).grid(row=2, column=2, stick='wesn')
button_1 = tkinter.Button(windows, text=1, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(1)).grid(row=3, column=0, stick='wesn')
button_2 = tkinter.Button(windows, text=2, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(2)).grid(row=3, column=1, stick='wesn')
button_3 = tkinter.Button(windows, text=3, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(3)).grid(row=3, column=2, stick='wesn')
button_0 = tkinter.Button(windows, text=0, bd=5, font=('Ink Free',15,'bold'), command=lambda: digit(0)).grid(row=4, column=0, stick='wesn')
button_plus = tkinter.Button(windows, text='+', bd=5, font=('Ink Free',15,'bold'), command=lambda :make_operation('+')).grid(row=1, column=3, stick='wesn')
button_minus = tkinter.Button(windows, text='-', bd=5, font=('Ink Free',15,'bold'), command=lambda :make_operation('-')).grid(row=2, column=3, stick='wesn')
button_mul = tkinter.Button(windows, text='*', bd=5, font=('Ink Free',15,'bold'), command=lambda :make_operation('*')).grid(row=3, column=3, stick='wesn')
button_delenie = tkinter.Button(windows, text='/', bd=5, font=('Ink Free',15,'bold'), command=lambda :make_operation('/')).grid(row=4, column=3, stick='wesn')
button_ravno = tkinter.Button(windows, text='=', bd=5, font=('Ink Free',15,'bold'), command=calculate).grid(row=4, column=1, stick='wesn')
button_clear = tkinter.Button(windows, text='C', bd=5, font=('Ink Free',15,'bold'), command=clear_result).grid(row=4, column=2, stick='wesn')
# Задаем минимальный размер колонок
windows.grid_columnconfigure(0, minsize=70)
windows.grid_columnconfigure(1, minsize=70)
windows.grid_columnconfigure(2, minsize=70)
windows.grid_columnconfigure(3, minsize=70)
# Устанавливаем размер строк
windows.grid_rowconfigure(0, minsize=30)
windows.grid_rowconfigure(1, minsize=70)
windows.grid_rowconfigure(2, minsize=70)
windows.grid_rowconfigure(3, minsize=70)
windows.grid_rowconfigure(4, minsize=70)

windows.mainloop()
