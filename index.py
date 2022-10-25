from tkinter import *
from tkinter import ttk


root = Tk()

root.title('Парсер товаров Везувий')
root.iconbitmap('parser.ico')
root.geometry('650x450+700+300')
root.update_idletasks()

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control, padding=[5, 5])
tab2 = ttk.Frame(tab_control, padding=[5, 5])

tab_control.add(tab1, text="Категорий")
tab_control.add(tab2, text="По ссылкам")

descripTab1 =  """
    Парсинг категорий товаров c cайтов производителя отопительного оборудования Везувий: 
    - vezuviy.su 
    - everest-pech.com
    - etna-pech.ru
    Для парсинга товаров небхдимо указать ссылку на категорию товаров на одном из указанных сайтов. 
"""

lb1 = Label(tab1, text=descripTab1, justify=LEFT, font=("Arial", 10))
lb1.grid(column=0, row=0)

lb1_label = Label(tab1, text='Укажите ссылку на категорию товаров:', justify=LEFT, font=("Arial", 10), anchor=NW)

lb1_label.grid(column=0, row=1)




lb2 = Label(tab2, text="Парсинг по ссылкам на товары Везувий")
lb2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# root.config(bg='#000')
# root['bg'] = 'red'

root.mainloop()







