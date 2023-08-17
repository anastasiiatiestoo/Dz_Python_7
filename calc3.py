# Калькулятор
import tkinter as tk

win = tk.Tk()
win.config(bg='#D4FFD4')
win.title('Калькулятор')
win.geometry('270x280+100+200')
win.resizable(False,False)

# Функции
def counting_the_response():
    screen = calc.get()
    calc.delete(0, tk.END)
    answer = (eval(screen))
    calc.insert((tk.END), answer)

def add_characters(characters):
    calc.insert((tk.END), characters)

def add_digit(digit):
    calc.insert((tk.END),digit)

def clear():
    calc.delete(0,tk.END)
    calc.insert(0,0)

calc = tk.Entry(win,bg='#A6FFFD',font=('Arial Black',15),bd=5)
calc.grid(row=0, column=0,columnspan=4)

# Кнопочки
tk.Button(text='1',bg='#FF8A8A',bd=10,command= lambda : add_digit(1)).grid(row=1, column=0,sticky='wens',padx=5,pady=5)#кнопка с цифрой 1
tk.Button(text='2',bg='#FF8A8A',bd=10,command= lambda : add_digit(2)).grid(row=1, column=1,sticky='wens',padx=5,pady=5)#кнопка с цифрой 2
tk.Button(text='3',bg='#FF8A8A',bd=10,command= lambda : add_digit(3)).grid(row=1, column=2,sticky='wens',padx=5,pady=5)#кнопка с цифрой 3
tk.Button(text='4',bg='#FF8A8A',bd=10,command= lambda : add_digit(4)).grid(row=2, column=0,sticky='wens',padx=5,pady=5)#кнопка с цифрой 4
tk.Button(text='5',bg='#FF8A8A',bd=10,command= lambda : add_digit(5)).grid(row=2, column=1,sticky='wens',padx=5,pady=5)#кнопка с цифрой 5
tk.Button(text='6',bg='#FF8A8A',bd=10,command= lambda : add_digit(6)).grid(row=2, column=2,sticky='wens',padx=5,pady=5)#кнопка с цифрой 6
tk.Button(text='7',bg='#FF8A8A',bd=10,command= lambda : add_digit(7)).grid(row=3, column=0,sticky='wens',padx=5,pady=5)#кнопка с цифрой 7
tk.Button(text='8',bg='#FF8A8A',bd=10,command= lambda : add_digit(8)).grid(row=3, column=1,sticky='wens',padx=5,pady=5)#кнопка с цифрой 8
tk.Button(text='9',bg='#FF8A8A',bd=10,command= lambda : add_digit(9)).grid(row=3, column=2,sticky='wens',padx=5,pady=5)#кнопка с цифрой 9
tk.Button(text='0',bg='#FF8A8A',bd=10,command= lambda : add_digit(0)).grid(columnspan=2,row=4, column=0,sticky='wens',padx=5,pady=5)#кнопка с цифрой 0

# Кнопки операции
tk.Button(text='+',bg='#FF8A8A',bd=10,command= lambda : add_characters("+")).grid(row=1, column=3,sticky='wens',padx=5,pady=5)#кнопка с знаком +
tk.Button(text='-',bg='#FF8A8A',bd=10,command= lambda : add_characters("-")).grid(row=2, column=3,sticky='wens',padx=5,pady=5)#кнопка с знаком -
tk.Button(text='*',bg='#FF8A8A',bd=10,command= lambda : add_characters("*")).grid(row=3, column=3,sticky='wens',padx=5,pady=5)#кнопка с знаком *
tk.Button(text='/',bg='#FF8A8A',bd=10,command= lambda : add_characters("/")).grid(row=4, column=3,sticky='wens',padx=5,pady=5)#кнопка с знаком /

# Кнопки равенства и очистки
tk.Button(text='=',bg='#FF8A8A',bd=10,command= counting_the_response).grid(row=4, column=2,sticky='wens',padx=5,pady=5)#кнопка с знаком =
tk.Button(text='с',bg='#FF8A8A',bd=10,command= clear).grid(row=4, column=3,sticky='wens',padx=5,pady=5)#кнопка с знаком с

# Размеры
win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

# Запуск
win.mainloop()
