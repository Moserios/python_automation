import datetime as dt

# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
date = "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
date_python = dt.datetime.strptime(date, "%b %d, %Y - %H:%M:%S")

# 1. Распечатайте полное название месяца из этой даты
print(date_python.strftime("%B"))
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
print(date_python.strftime("%d.%m.%Y, %H:%M"))

# List comprehension
# Дан такой кусок прайс листа: (Копируйте эту переменную (константу) в код прямо как есть)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# При помощи генераторов превратите этот текст в словарь такого вида:
converted = list(map(lambda x: x.split(" "), PRICE_LIST.splitlines()))
print(converted)
finished_dict = {key: int(value.rstrip("р")) for (key, value) in converted}
print(finished_dict)

# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)
