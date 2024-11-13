# Задача 1. Привести к целому типу -1.6, 2.99
def to_int (*args):
   return int(*args)
print(to_int(-1.6))
print(to_int(2.99))

#Задача 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
def new_text(text):
    return text.replace("#", "/")
print(new_text("www.my_site.com#about"))

#Задача 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

def my_str(text):
    return text+"ing"
print(my_str("stroka"))

#Задача 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

def hello(my_name):
    new_name = my_name.split()
    my_new_name = f"{new_name[1]} {new_name[0]}"
    return my_new_name
print(hello("Ivanou Ivan"))

#Задача 5. Напишите программу, которая удаляет пробел в начале, в конце строки
def poem(word):
    return word.strip()
print(poem("    Белая береза под моим окном. Принакрыла ветки, словно серебром. "))

#Задача 6. Создайте словарь, связав его с переменной school,
# и наполните его данными которые # бы отражали количество учащихся в десяти
# разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

def school_back():
    school = {"1a": 25, "1б": 27, "2a": 23, "2б": 25, "3а": 24, "3б": 19, "4а": 25, "4б": 22, "5а": 19, "5б": 18}
    return school
print (school_back())

#Задача 7. Создайте список и извлеките из него списка второй элемент
def my_list():
    own_list = [10,5,2]
    return own_list[1]
print (my_list())

#Задача 8. Вывести входит ли строка1 в строку2 (пример: employ и employment )
def s1_in_s2(s1,s2):
    return s1 in s2
print (s1_in_s2("employ","employment"))

"""Задача 9. Вывести нужные символы. x = "My name is Agent Smith"
print(x[?]) #y
print(x[?:?:?]) #nesgt"""

def symbol():
    x = "My name is Agent Smith"
    return x[1], x[3:16:3]
print(symbol())

"""Задача 10. сть массив чисел. Известно, что каждое число в этом массиве имеет
пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число"""

def array():
    arr = [1, 5, 2, 9, 2, 9, 1]
    i = 0
    while i < len(arr):
        i += 1
    uniq1 = arr.count(arr[0])
    if uniq1 == 1:
        return arr[0]
    uniq2 = arr.count(arr[1])
    if uniq2 == 1:
        return arr[1]
    uniq3 = arr.count(arr[2])
    if uniq3 == 1:
        return arr[2]
    uniq4 = arr.count(arr[3])
    if uniq4 == 1:
        return arr[3]
print(array())