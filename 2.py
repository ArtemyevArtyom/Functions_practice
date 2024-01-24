"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

def uniq_unicode(my_str: str) -> list[str]:
    my_list = sorted(list(set([ord(el) for el in my_str])), reverse=True)
    return my_list

def uniq_number(my_str: str) -> list:
    lst = sorted({el: ord(el) for el in set(my_str)}.items(), key=lambda x: x[1], reverse=True)
    return lst

print(ord("s"))
print(ord(" "))
print(uniq_number("sdf sdfds"))
print(uniq_unicode("sdf sdfds"))