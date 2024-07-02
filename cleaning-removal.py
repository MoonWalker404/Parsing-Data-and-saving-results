import requests
from bs4 import BeautifulSoup
url = "https://"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("tr")
# tr - каждый ряд таблицы
# td - каждая ячейка внутри ряда таблицы
data = []

for row in rows:
    cols = row.find_all("td")
# Используем укороченный вариант цикла for
# Для удаления пробелов и других лишних символов используем функцию strip
    cleaned_cols = [col.text.strip() for col in cols]
# Чтобы удалить пробелы, оставляем ()
# Чтобы удалить какие-то символы из начала и конца, пишем ('то-что-надо-удалить')
    data.append(cleaned_cols)
# Функция append добавляет в список.
    print(data)



data = [
        ['100', '200', '300']
        ['400', '500', '600']
    ]
# С сайта мы получаем именно списки.
numbers = []

# 2.Используем функции float или int, чтобы преобразовать данные.

for row in data:
    for text in row:
        number = int(text)
        numbers.append(number)

print(numbers)

# Чаще всего преобразования — это просто преобразование одного типа данных в другой.
# Отфильтруем данные — это можно делать через обычные условия.
# У нас также есть двумерный список, содержащий другие списки.

data = [

    [100, 110, 120]
    [400, 500, 600]
    [150, 130, 140]

    ]

list = []

# 2. Используем цикл for и условие:

for row in data:
    for item in row:
        if item > 190:
            list.append(item)

print(list)