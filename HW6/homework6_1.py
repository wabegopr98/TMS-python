"""Дан файл целых чисел, содержащий не менее 4 элементов. Вывести первый, второй,
предпоследний и последний элементы данного файла. Если чисел меньше 3 выводить ошибку"""
with open("text.txt", "w") as file1:
    numbers = list(range(1,5))
    for number in numbers:
        file1.write(str(number) + " ")
with open("text.txt", "r") as file1:
     for line in file1:
         s = line.split()
         s = "".join(s)
         if len(s)<3:
             print("Слишком мало символов. Нужно больше!")

         else:
            print(s[0])
            print(s[1])
            count = len(s)
            print(s[count-1])
            print(s[count-2])
