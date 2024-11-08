"""Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
Извлеките из строки первый символ, затем последний, третий с начала и третий с
конца. Измерьте длину вашей строки."""

my_str = ("I've become so numb")
print(my_str[0])
str_len = len(my_str)
print(str_len)
print(my_str[str_len-1])
print(my_str[2])
print(my_str[str_len-3])
