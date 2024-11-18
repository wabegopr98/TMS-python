#Даны три целых числа. Найти количество положительных чисел в исходном
#наборе.

a = int(input ("Введите число "))
b = int(input ("Введите число "))
c = int(input ("Введите число "))
plus = 0

mylist = [a,b,c]
for x in mylist:
    if x > 0:
        plus += 1
    else:
        plus = plus
print(plus)
