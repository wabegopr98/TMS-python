"""1 Создайте два любых списка и свяжите их с переменными.
2 Извлеките из первого списка второй элемент.
3 Измените во втором списке последний элемент. Выведите список на экран.
4 Соедините оба списка в один, присвоив результат новой переменной. Выведите
получившийся список на экран.
5 "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
обоих первых списков. Срез свяжите с очередной новой переменной. Выведите
значение этой переменной.
6 Добавьте в список два новых элемента и снова выведите его."""

spisok1 = [1,2,3,4,5,6]
spisok2 = [9,8,7,6,5,4]

print(spisok1[1])
spisok2.pop(5)
print(spisok2)
spisok2.append(10)
print(spisok2)

spisok3 = spisok1 + spisok2
print(spisok3)

spisok4 = [spisok1.pop(0), spisok1.pop(2), spisok2.pop(0), spisok2.pop(4)]
print(spisok4)
spisok4.append(50)
spisok4.append(100)
print(spisok4)