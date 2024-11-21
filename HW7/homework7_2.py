"""Создать лямбда функцию, которая принимает на вход список имен и выводит их
в формате "Hello, {name}" в другой список"""

myname1 = input("Как вас зовут? ")
myname2 = input("Как вас зовут? ")
myname3 = input("Как вас зовут? ")

names_list = [myname1, myname2,myname3]

new_names_list = list(map(lambda name: f"Hello, {name}", names_list))
print(new_names_list)