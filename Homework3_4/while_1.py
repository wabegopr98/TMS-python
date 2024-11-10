# Дано число N. Найти произведение всех чисел от 0 до N.

N = int(input("Введите ваше число "))
i = 0
multiply=1

if(N<=0):
    print("Нам нужно положительное число")

while(i<N-1) :

    i += 1
    multiply *=i
    print(multiply)






