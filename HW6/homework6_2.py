"""Дан файл целых чисел. Создать два новых файла, первый из которых содержит
четные числа из исходного файла, а второй - нечетные. Если четные или нечетные
 числа в исходном файле отсутствуют, то соответствующий результирующий файл
 оставить пустым"""

with open("list.txt", "w") as file1:
    numbers = list(range(100, 150))
    for number in numbers:
        file1.write(str(number) + " ")
with open("list.txt", "r") as file1:
    for line in file1:
        s = line.split(" ")
        len_line = len(s) #вычисляем количество наших последних элементов, чтоб удалить лишний пробел
        s.pop((len_line-1))

        a = []
        b = []

        for symbol in s:
            a = [str(symbol) for symbol in s if int(symbol) % 2 == 0]
            b = [str(symbol) for symbol in s if int(symbol) % 2 != 0]
            break
        if a:
            with open("even_numbers", "w") as file2:
                file2.write(str(a))
        if b:
            with open("odd_numbers", "w") as file3:
                 file3.write(str(b))
