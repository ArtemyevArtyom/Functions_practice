"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


lst = [1, 3, -5, 7, 5, 8, 4, -9, 2]

def my_func(lst: list, l, r):

    if l >= r:
        print('Элементов нет')
        return
    elif l < 0 and r > len(lst):
        return sum(lst)
    elif l < 0:
        return sum(lst[:r])
    elif r > len(lst):
        return sum(lst[l+1:])
    else:
        return sum(lst[l + 1:r])

print(my_func(lst, 2, 6))