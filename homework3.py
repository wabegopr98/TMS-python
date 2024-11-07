# Задача 1. Привести к целому типу -1.6, 2.99
print(int(-1.6))
print(int(2.99))

#Задача 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
text = "www.my_site.com#about"
new_text = text.replace("#", "/")
print(new_text)

#Задача 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
my_str = "stroka"
print(my_str + "ing")

#Задача 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name_surname = "Ivanou Ivan"
new_name = name_surname.split()
my_new_name = f"{new_name[1]} {new_name[0]}"
print(my_new_name)

#Задача 5. Напишите программу, которая удаляет пробел в начале, в конце строки
some_words = "  Белая береза под моим окном. Принакрыла ветки, словно серебром."
print(some_words.strip())

"""Задача 6. Создайте словарь, связав его с переменной school,
# и наполните его данными которые # бы отражали количество учащихся в десяти
# разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.)."""

school = {"1a": 25, "1б": 27, "2a": 23, "2б": 25, "3а": 24, "3б": 19, "4а": 25, "4б": 22, "5а": 19, "5б": 18}
print(school)

#Задача 7. Создайте список и извлеките из него списка второй элемент

my_list = [10,100,1000]
print(my_list[1])

#Задача 8. Вывести входит ли строка1 в строку2 (пример: employ и employment )
str1 = "employment"
str2 = "employ"
print(str2 in str1)

"""Задача 9. Вывести нужные символы
x = "My name is Agent Smith"
print(x[?]) #y
print(x[?:?:?]) #nesgt"""

x = "My name is Agent Smith"
print (x[1])
print(x[3:16:3])