"""
Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""

import string
def out_str_with_num(my_str: str) -> str:
    punct = f'-{string.punctuation}'
    for item in punct:
        my_str = my_str.replace(item, ' ')
    lst_str = my_str.lower().split()
    shift = len(max(lst_str))
    for n, el in enumerate(sorted(lst_str, reverse=True), 1):
        print(f"{n}. {el:>{shift}}")


out_str_with_num(input("something: "))