"""1 Создайте словарь, связав его с переменной school, и наполните его данными,
которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
2б, 6а, 7в и т.д.).
2 Узнайте сколько человек в каком-нибудь классе.
3 Представьте, что в школе произошли изменения, внесите их в словарь:
◦ в трех классах изменилось количество учащихся;
◦ в школе появилось два новых класса;
◦ в школе расформировали один из классов.
4 Выведите содержимое словаря на экран."""

school = {"1а" : 24, "1б" : 20, "1в" : 22, "2а" : 23, "2б" : 19, "3а" : 21, "3б": 17, "4а" : 20, "4б" : 25, "4в" : 18}

my_students = school["1а"]
print(my_students)

school["1б"] = 21
school["2а"] = 24
school["3б"] = 18
print(school["1б"])
print(school["2а"])
print(school["3б"])

school["5а"] = 24
school["5б"] = 24
print(school.items())

school.pop("1в")
print(school.items())