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

multiply_positive = 1
sum_negative = 0
count_negative = 0


my_numbers = [a,b,c,d,e,f,g,h,i,j]
# if my_numbers.__contains__(0):
#     print(multiply_positive == 0)

for x in my_numbers :
    if(x>0):
        multiply_positive*=x
    elif(x<0):
        sum_negative+=x
        count_negative+=1
    elif(x==0):
        sum_negative = sum_negative
        multiply_positive = 0
        count_negative = count_negative
    else:
        print("ошибка данных")

print(multiply_positive)
print(sum_negative)
print(count_negative)

