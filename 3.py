"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""
def func_dict(my_str: str) -> dict:

    my_dict = {chr(int(el)): int(el) for el in sorted(my_str.split())}
    return my_dict

print(func_dict("8 3"))