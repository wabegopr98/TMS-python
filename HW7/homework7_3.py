"""Напишите генератор, который принимает список numbers = [34.6, -203.4, 44.9,
 68.3, -12.2, 44.6, 12.7] и возвращает новый список только с положительными числами"""

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers  = [number for number in numbers if number > 0]
print(positive_numbers)