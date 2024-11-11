"""Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
уникальное число"""

array = [1,5,2,9,2,9,1]
for x in array:
    uniq1 = array.count(array[0])
    if uniq1 == 1:
        print(array[0])
    uniq2 = array.count(array[1])
    if uniq2 ==1:
        print(array[1])
    uniq3 = array.count(array[2])
    if uniq3 ==1:
        print(array[2])
    uniq4 = array.count(array[3])
    if uniq4 ==1:
        print(array[3])
    break