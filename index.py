from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from module import *
import os
import pyperclip


root = Tk()
root.title('Парсер товаров Везувий')
root.iconbitmap('parser.ico')
root.geometry('650x450+700+300')
root.update_idletasks()

# Кнопка - открыть деррикторию с результатами парсинга
def open_folder():
    os.startfile('upload')

# Кнопка -  очистить все, удалить информационные сообщения
def clean_all():
    tb1_entry.delete(0, END)
    lb1_valid['text'] = ''
    lb1_label_info_1['text']=''
    lb1_label_info_2['text'] = ''
    lb1_label_info_3['text'] = ''

# Вызов и обработка всплывающего меню - вставка/копирование/очистка поля ввода ссылки на категорию товаров
def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

x = 0
y = 0

def inToFromBuffer():
    buffer = pyperclip.paste()
    if buffer: tb1_entry.insert(END, buffer)

def clearField():
    tb1_entry.delete(0, END)
    lb1_valid['text'] = ''

def copyToBuffer():
    buffer = tb1_entry.get()
    if buffer: pyperclip.copy(buffer)

# Вызов и обработка всплывающего меню - вставка/копирование/очистка поля ввода ссылки на список ссылок

def popup_text(event):
    global x, y
    x = event.x
    y = event.y
    menu2.post(event.x_root, event.y_root)
def inToFromBuffer_text():
    buffer = pyperclip.paste()
    if buffer: tb2_text.insert(END, buffer)
def copyToBuffer_text():
    buffer = tb2_text.get("1.0", END)
    if buffer: pyperclip.copy(buffer)
def clearField_text():
    tb2_text.delete("1.0", END)

# Кнопка очистить текстовое поле - список ссылок:
def clean_links():
    tb2_text.delete("1.0", END)
    lb2_valid['text'] = ''
    lb2_valid['fg'] = '#000000'



# 1.  Прарсинг товаров по ссылке на категорию:
# 1.1 Валидация ссылки на категорию товаров
def startPars():
    if lb1_valid['text']:
        lb1_valid['text'] = ''
    if lb1_label_info_1['text']:
        lb1_label_info_1['text']=''
    if lb1_label_info_2['text']:
        lb1_label_info_2['text'] = ''
    if lb1_label_info_3['text']:
        lb1_label_info_3['text'] = ''

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

    # Валидация пройдена, старт персинга
    lb1_label_info_1['text'] = 'Старт парсинга...'

    # 1.1 Получаем ссылки на товары указанной категории
    a = DataGetLinks(link)
    listLinks = a.get()

    # 1.2 Парсинг данных по полученным ссылкам, получаем данные количества товаров
    if len(listLinks) > 0:
        resault = []
        productCount = 0
        lb1_label_info_1['text'] = f'Получены ссылоки на товары: {len(listLinks)}.'
        for itemUrl in listLinks:
            page = DataPage(itemUrl)
            item = page.get()
            if item['is']:
                tpl = item.copy()
                resault.append(tpl)
                productCount += 1

        if len(resault) > 0:
            lb1_label_info_2['text'] = 'Полученны данные товаров: ' + str(productCount)
            # 1.3 Запись полученных данных в excel файл
            line = ExcelFile(resault)
            res = line.get()
            if res:
                lb1_label_info_3['text']='Создан файл: ' + res
                return # Парсинг завершен
        else:
            lb1_label_info_3['text'] = f"Данные товаров не получены"
            lb1_label_info_3['foreground']='#db0303'
            return
    else:
        lb1_valid['text'] = 'Не получены ссылки на товары'
        return


# 2.  Прарсинг товаров по списку ссылок:
def startParsByLinks():
    if lb2_valid['text']:
        lb2_valid['text'] = ''
        lb2_valid['fg'] = '#000000'
    if lb2_label_info_2['text']:
        lb2_label_info_2['text'] = ''
    listLinks = []
    resault =[]
    productCount = 0

    notDomens = 0  # Количество: не ссответсвует доменам
    data = tb2_text.get("1.0", END)

    if data:
        lines = data.split('\n')
        for line in lines:
            link = re.sub("^\s+|\n|\r|\s+$", '', line)
            if not line:
                continue
            if not isLink(link):
                continue
            if not isLinkCorrect(link):
                notDomens += 1
                continue
            listLinks.append(link)

    if len(listLinks) > 0:
        #answer_1 = ''
        if not notDomens: answer_1 = f'Получено: {len(listLinks)} ссылок для парсинга.'
        else: answer_1 = f'Получено: {len(listLinks)} ссылок для парсинга. В списке ссылок {notDomens} - не соответсвуют доменам Везувий'
        lb2_valid['text'] = answer_1
        lb2_valid['fg'] = '#000000'

        for itemUrl in listLinks:
            page = DataPage(itemUrl)
            item = page.get()
            if item['is']:
                tpl = item.copy()
                resault.append(tpl)
                productCount += 1

        if len(resault) > 0:
            line = ExcelFile(resault)
            res = line.get()
            if productCount > 0 and res:
                lb1_label_info_2['text'] = f"Получен данные товаров: {productCount}, создан файл {res}"
                lb1_label_info_2['fg'] = '#000000'
            else:
                lb1_label_info_2['text'] = 'Данные товаров не получены'
                lb1_label_info_2['fg'] = '#db0303'
    else:
        lb2_valid['text'] = 'Нет ссылок для парсинга'
        lb2_valid['fg'] = '#db0303'
        return

#  --- GUI TKINTER
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

tb1_entry.bind("<Button-3>", popup)
menu = Menu(tearoff=0)
menu.add_command(label="Вставить", command=inToFromBuffer)
menu.add_command(label="Копировать", command=copyToBuffer)
menu.add_command(label="Очистить", command=clearField)


tb1_btn_start = ttk.Button(tab1, text="Start", command=startPars)
tb1_btn_start.place(x=382, y=129, anchor=NW)

folder_open = PhotoImage(file="folder-open.png")
tb1_btn_folder = ttk.Button(tab1, image=folder_open, width=20, command=open_folder)
tb1_btn_folder.place(x=462, y=129, anchor=NW)

trash = PhotoImage(file="trash-can.png")
tb1_btn_trash = ttk.Button(tab1, image=trash, width=20, command=clean_all)
tb1_btn_trash.place(x=495, y=129, anchor=NW)

# Вывод информации. Tab1 - валидайия и результаты парсинга
lb1_valid = Label(tab1, text='', justify=LEFT, fg='#db0303', font=("Arial", 9, "italic"), anchor=NW)
lb1_valid.place(x=10, y=155, anchor=NW)

lb1_label_info_1 = Label(tab1, text='', justify=LEFT, font=("Arial", 10, 'italic'))
lb1_label_info_1.place(x=10, y=175, anchor=NW)

lb1_label_info_2 = Label(tab1, text='',  justify=LEFT, font=("Arial", 10, 'italic'))
lb1_label_info_2.place(x=10, y=195, anchor=NW)

lb1_label_info_3 = Label(tab1, text='', justify=LEFT, font=("Arial", 10, 'italic'), anchor=NW)
lb1_label_info_3.place(x=10, y=215, anchor=NW)


# ------------**********-------------------

# Second tab2
lb2 = Label(tab2, text="Укажите список ссылок товаров для парсинга:", justify=LEFT, font=("Arial", 9), padx=10)
lb2.pack(anchor=NW)


# Текстовое поле со скролом
tb2_frame = ttk.Frame(tab2)
tb2_frame.pack(fill=X, anchor=NW)

tb2_text = Text(tb2_frame, font=("Arial", 9),  padx=10, pady=10,  width=30, height=15)
tb2_text.pack(fill=X, expand=1, side=LEFT, anchor=NW)

tb2_scroll = Scrollbar(tb2_frame, command=tb2_text.yview)
tb2_scroll.pack(fill=Y, side=LEFT)
tb2_text.config(yscrollcommand=tb2_scroll.set)

# Вызов контестного меню на поле списка ссылок
tb2_text.bind("<Button-3>", popup_text)
menu2 = Menu(tearoff=0)
menu2.add_command(label="Вставить", command=inToFromBuffer_text)
menu2.add_command(label="Копировать", command=copyToBuffer_text)
menu2.add_command(label="Очистить", command=clearField_text)


# Кнопки управления
tb2_frame_btn = ttk.Frame(tab2, height=45, padding=[8, 10, 6, 5])
tb2_frame_btn.pack(fill=X, expand=0,  anchor=NW)

tb2_btn_start = ttk.Button(tb2_frame_btn, text="Start", command=startParsByLinks)
tb2_btn_start.place(x=443, y=0, anchor=NW)

tb2_btn_folder = ttk.Button(tb2_frame_btn, image=folder_open, width=20, command=open_folder)
tb2_btn_folder.place(x=525, y=0, anchor=NW)

tb2_btn_trash = ttk.Button(tb2_frame_btn, image=trash, width=20, command=clean_links)
tb2_btn_trash.place(x=560, y=0, anchor=NW)

# Вывод информации. Tab2 - валидайия и результаты парсинга
tb2_frame_info = ttk.Frame(tab2, height=75, padding=[8, 10, 0, 0])
tb2_frame_info.pack(fill=X, expand=0,  anchor=NW)

lb2_valid = Label(tb2_frame_info, text='', justify=LEFT, font=("Arial", 9, "italic"), anchor=NW)
lb2_valid.place(x=0, y=0, anchor=NW)

lb2_label_info_2 = Label(tb2_frame_info, text='', justify=LEFT, font=("Arial", 10, 'italic'))
lb2_label_info_2.place(x=0, y=20, anchor=NW)

tab_control.pack(expand=1, fill='both')

root.mainloop()