"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""

from random import randint
from timeit import timeit

orig_list = [randint(-100, 100) for _ in range(10)]

def bubble_sort(orig_list):

    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] > orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1

    return orig_list

print(bubble_sort(orig_list[:]))
print(orig_list)
print(timeit('bubble_sort(orig_list[:])', globals=globals(), number=100))