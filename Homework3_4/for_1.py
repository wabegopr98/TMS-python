#Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
#включительно.

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
sum = 0
for x in range(a,b+1):
    sum+=x
print(sum)