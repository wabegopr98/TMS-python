# Найти сумму всех натуральных чисел в от A до B

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
sum = 0

for x in range(a,b):
    if(x<=0):
        sum=sum
    else:
        sum+=x
print(sum)