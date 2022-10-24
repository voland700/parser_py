from module import DataPage
from module import DataGetLinks
from module import ExcelFile

url = input('Введите ссылку на категорию товаров: ' )
resault = []


a = DataGetLinks(url)
listLinks = a.get()

linkCount = len(listLinks)
productCount = 0

print(f"Получены {linkCount} ссылки на товары. Приступаем к парсингу данных")

if len(listLinks)>0:

    for itemUrl in listLinks:
        page = DataPage(itemUrl)
        item = page.get()
        if item['is']:
            tpl = item.copy()
            resault.append(tpl)
            productCount +=1

if len(resault)>0:
    line = ExcelFile(resault)
    res = line.get()


print(f"Данные записаны. Создан файл: {res}")
print("")
print('-----***************------')
print(f"Получено {linkCount} -ссылок, Произвден парсинг {productCount} товаров")

