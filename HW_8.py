# 1. Импортируйте `full_dict` из файла `Marvel.py`.
from marvel import  full_dict
from pprint import pprint
from typing import Dict, Any

# 2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.
user_ints = list(map(lambda x: int(x) if x.isdigit() else None, input('Введите числа через пробел: ').split()))

# 3. Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.
filtered_dict = {id: data for id, data in full_dict.items() if id in user_ints}
# print(filtered_dict)

# 4. Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.
directors = {film['director'] for film in filtered_dict.values()}

# 5. С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку. **(Опционально)**
str_year_dict = {id: {**data, 'year': str(data['year'])} for id, data in filtered_dict.items()}

# 6. Используйте `filter`, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву `Ч`.
print("\nПроверяем названия фильмов:")
for id, data in filtered_dict.items():
    print(data['title'])

ch_films = dict(filter(lambda x: x[1]['title'][0] in ['Ч', 'ч'],  filtered_dict.items()))


# 7. Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку.
sorted_by_year = dict(sorted(filtered_dict.items(), key=lambda x: (x[1]['year'], x[1]['title'])))

# 8. Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.
if filtered_dict:
    sorted_by_year_title = dict(sorted(filtered_dict.items(), key=lambda x: (x[1]['year'], x[1]['title'])))

else:
    sorted_by_year_title = {}

# 9. Напишите однострочник, который отфильтрует и отсортирует `full_dict` с использованием `filter` и `sorted`.
filtered_sorted = dict(sorted([(k,v) for k,v in full_dict.items() if v['year'] != 'TBA' and int(v['year']) > 2010], key=lambda x: x[1]['director']))
                           

# 10. **Опционально:** Добавьте аннотацию типов для переменных, содержащих результаты, и проверьте код с помощью `mypy`. Оставьте комментарий о успешной проверке.

sorted_by_year_title: Dict[int, Dict[str, Any]] = sorted_by_year_title

# Проверка с помощью mypy
# mypy HW_8.py

# mypy check passed successfully: no issues found

# 11. Сделайте красивый вывод результатов с использованием `pprint`, добавив подпись о том, какое задание выполнено.
print("\n" + "=" * 50)
print("Задание 2 - Список чисел от пользователя:")
print(user_ints)

print("\n" + "="*50)
print("Задание 3 - Отфильтрованный словарь по ID:")
pprint(filtered_dict)

print("\n" + "="*50)
print("Задание 4 - Уникальные режиссеры:")
pprint(directors)

print("\n" + "="*50)
print("Задание 5 - Словарь с годами в строковом формате:")
pprint(str_year_dict)

print("\n" + "="*50)
print("Задание 6 - Фильмы на букву 'Ч':")
pprint(ch_films)

print("\n" + "="*50)
print("Задание 7 - Сортировка по году:")
pprint(sorted_by_year)

print("\n" + "="*50)
print("Задание 8 - Сортировка по году и названию:")
pprint(sorted_by_year_title)

print("\n" + "="*50)
print("Задание 9 - Фильтрация (год > 2010) и сортировка по режиссеру:")
pprint(filtered_sorted)