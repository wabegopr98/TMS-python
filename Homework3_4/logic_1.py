"""1 Присвойте двум переменным любые числовые значения.
2 Составьте четыре сложных логических выражения с помощью оператора and, два из
которых должны давать истину, а два других - ложь.
3 Аналогично выполните п. 2, но уже используя оператор or.
4 Попробуйте использовать в сложных логических выражениях работу с переменными
строкового типа."""
a = 7
b = -10

print(a>10 & b>=-10)
print(a>-15 & b<-15)
print(a<10 & b>-15)
print(a>0 & b >0)

print(a<10 or b > 0)
print(a>10 or b<0)
print(a>10 or b>0)
print(a<0 or b>0)

long_word = "Knowledge"
print (long_word.__contains__("n") & long_word.__contains__("e"))
print(long_word.__contains__("d") & long_word.__contains__("f"))
print(long_word.__contains__("s") or long_word.__contains__("l"))
print(long_word.__contains__("x") or long_word.__contains__("c"))