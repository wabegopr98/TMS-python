"""Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое
число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
массу тела в килограммах."""

weight = int(input("Введите число от 1 до 5 "))
weight_num = int(input("Введите вес объекта "))

if(weight==1):
    print("Вес объекта в киллограммах - " + str(weight_num))
elif(weight==2):
    kg_weight = weight_num / 1000000
    print("Вес объекта в киллограммах - " + str(kg_weight))
elif(weight==3):
    kg_weight = weight_num / 1000
    print("Вес объекта в киллограммах - " + str(kg_weight))
elif(weight==4):
    kg_weight = weight_num*1000
    print("Вес объекта в киллограммах - " + str(kg_weight))
elif(weight==5):
    kg_weight = weight_num*100
    print("Вес объекта в киллограммах - " + str(kg_weight))
else:
    print("Вы ввели неправильную цифру. Попробуйте еще раз. ")