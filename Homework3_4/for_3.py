#Найти произведение положительных, сумму и количество отрицательных
#из 10 введенных целых значений.

a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
d = int(input("Введите число "))
e = int(input("Введите число "))
f = int(input("Введите число "))
g = int(input("Введите число "))
h = int(input("Введите число "))
i = int(input("Введите число "))
j = int(input("Введите число "))

multiplyPositive = 1
sumNegative = 0
countNegative = 0


myNumbers = [a, b, c, d, e, f, g, h, i, j]

for x in myNumbers :
    if x > 0:
        multiplyPositive *= x
    elif x < 0:
        sumNegative += x
        countNegative += 1
    elif x == 0:
        sumNegative = sumNegative
        multiplyPositive = 0
        countNegative = countNegative

print(multiplyPositive)
print(sumNegative)
print(countNegative)
