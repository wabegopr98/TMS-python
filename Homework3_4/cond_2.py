#Даны три целых числа. Найти количество положительных чисел в исходном
#наборе.

a = int(input ("Введите число "))
b = int(input ("Введите число "))
c = int(input ("Введите число "))
plus = 0

if(a>0):
    plus+=1
else:
    plus = plus
if(b>0):
    plus +=1
else:
    plus=plus
if(c>0):
    plus+=1
else:
    plus=plus
print(plus)