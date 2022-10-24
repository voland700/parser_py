from tkinter import *

from tkinter import ttk


root = Tk()

root.title('Парсер товаров Везувий')
root.iconbitmap('parser.ico')
root.geometry('600x400+750+300')
root.update_idletasks()

btn = ttk.Button(text="Click") # создаем кнопку из пакета ttk
btn.pack()    # размещаем кнопку в окне



# root.config(bg='#000')
# root['bg'] = 'red'

root.mainloop()







