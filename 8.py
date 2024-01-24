"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

def change_val():
    val = globals().copy()
    my_val = {item: val[item] for item in val.keys() if not item.startswith('__')}
    for items in my_val.copy():
        if items.endswith("s") and len(items) != 1:
            my_val[items[:-1]] = my_val[items]
            my_val[items] = None
    print(my_val)

num = 1
tasks = 3
s = 4
res = ["sdf", "sdfsfw"]
change_val()