"""Дан файл целых чисел. Создать два новых файла, первый из которых содержит
четные числа из исходного файла, а второй - нечетные. Если четные или нечетные
 числа в исходном файле отсутствуют, то соответствующий результирующий файл
 оставить пустым"""

with open("list.txt", "w") as file1:
    numbers = list(range(1, 10))
    for number in numbers:
        file1.write(str(number) + " ")
with open("list.txt", "r") as file1:
    for line in file1:
        s = line.split()
        s = "".join(s)
        a = []
        b = []

        for symbol in s:
            if int(symbol) % 2 == 0:
                a+=symbol

            else:
                b+=symbol

            if a:
                with open("even_numbers", "w") as file2:
                    file2.write(str(a))
            if b:
                with open("odd_numbers", "w") as file3:
                    file3.write(str(b))
