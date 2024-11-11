#Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
#внука. И сколько при этом лет будет деду и внуку.

 grand_age = int(input("Введите возраст дедушки "))
 grandson_age = int(input("Введите возраст внука "))

 year_count = 0

 while grand_age>grandson_age *2:

     year_count+=1
     grand_age +=1
     grandson_age +=1

 print("Возраст дедушки - " + str(grand_age), "возраст внука - " + str(grandson_age))

