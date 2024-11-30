"""Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы"""
import datetime

start = datetime.datetime.now()
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
end = datetime.datetime.now()
fact_time = end - start
print(fact_time)

start = datetime.datetime.now()
def factorial_recursive(n):
    return 1 if n < 2 else n * factorial_recursive(n - 1)
end = datetime.datetime.now()
recurs_time = end - start
print(recurs_time)

start = datetime.datetime.now()
def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result
end = datetime.datetime.now()
gen_time = end - start
print(gen_time)

times = [fact_time, recurs_time,gen_time]
def best_result(result):
    return min(result)
best_time = best_result(times)
print(f"Найлучшее время экзекьюшена", best_time)
