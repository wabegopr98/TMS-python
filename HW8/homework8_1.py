n = int(input("Факториал какого числа нужно найти? "))
def factorial(n):
    result= 1
    while n >= 1:
        result *= n
        n-=1
    return result

print(factorial(n))

# x = int(input("Факториал какого числа нужно найти? "))
# def factorial_new(x):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_new(x-1)
# print(factorial_new(x))

def factorial(z):
    if z <= 1:
        return 1
    else:
        return z * factorial(z-1)
z = int(input("Введите число:"))
print(factorial(z))


from functools import reduce
print(reduce(lambda x, y: x*y, [x for x in range(1, int(input("Факториал какого числа нужно найти? "))+1)]))


