"""Есть строка: test_tring = "Hello world!", необходимо
●напечатать на каком месте находится буква w
●кол-во букв l
●Проверить начинается ли строка с подстроки: “Hello”
●Проверить заканчивается ли строка подстрокой: “qwe”"""

test_tring = "Hello world!"

i=0
while(i<len(test_tring)):
    if(test_tring.__contains__("w")):
        print(test_tring.index("w"))
        break
i+=1

num_l = test_tring.count("l")
print(num_l)
start = test_tring.startswith("Hello")
print(start)
end = test_tring.endswith("qwe")
print(end)