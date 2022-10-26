from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from module import *
import os
import sys


root = Tk()

root.title('Парсер товаров Везувий')
root.iconbitmap('parser.ico')
root.geometry('650x450+700+300')
root.update_idletasks()

def open_folder():
    os.startfile('upload')

def showMenuInsert(self):
    menu = Menu(tearoff=0)
    menu.add_command(label="Вставить")
    menu.place(x=15, y=133, anchor=NW)

def startPars():
    link = tb1_entry.get()
    if not isLink(link):
        lb1_valid['text'] = 'Укажите корректную ссылку на категорию товаров'
        return
    else:
        lb1_valid['text'] = ''

    if not isLinkCorrect(link):
        lb1_valid['text'] = 'Ссылка должна вести на сайты производителя Везувий'
        return
    else:
        lb1_valid['text'] = ''


    print(link)



tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control, padding=[5, 5])
tab2 = ttk.Frame(tab_control, padding=[5, 5])

tab_control.add(tab1, text="Категорий")
tab_control.add(tab2, text="По ссылкам")

# first tab1
descripTab1 =  """
    Парсинг категорий товаров c cайтов производителя отопительного оборудования Везувий: 
    - vezuviy.su 
    - everest-pech.com
    - etna-pech.ru
    Для парсинга товаров небхдимо указать ссылку на категорию товаров на одном из указанных сайтов. 
"""

lb1 = Label(tab1, text=descripTab1, justify=LEFT, font=("Arial", 10))
lb1.place(height=100,  relwidth=1)

lb1_label = Label(tab1, text='', justify=LEFT, font=("Arial", 8, "bold"), anchor=NW)
lb1_label.place(x=10, y=105, anchor=NW)

tb1_entry = ttk.Entry(tab1, justify=LEFT, font=("Arial", 11), width=45)
tb1_entry.place(x=10, y=130, anchor=NW)



tb1_btn_start = ttk.Button(tab1, text="Start", command=startPars)
tb1_btn_start.place(x=382, y=129, anchor=NW)

folder_open = PhotoImage(file="folder-open.png")
tb1_btn_folder = ttk.Button(tab1, image=folder_open, width=20, command=open_folder)
tb1_btn_folder.place(x=462, y=129, anchor=NW)

lb1_valid = Label(tab1, text='', justify=LEFT, fg='#db0303', font=("Arial", 9, "italic"), anchor=NW)
lb1_valid.place(x=10, y=155, anchor=NW)





# Second tab2
lb2 = Label(tab2, text="Парсинг по ссылкам на товары Везувий")
lb2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# root.config(bg='#000')
# root['bg'] = 'red'

root.mainloop()







