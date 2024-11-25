"""Даны 2 файла произвольного типа. Поменять местами их содержимое.
Файлы должны быть бинарными."""

with open("new_file1.bin", "wb") as file1:
    my_num = "100000101 00010101"
    file1.write(my_num.encode())

with open("new_file2.bin", "wb") as file2:
    my_num2 = "00101010 11010101"
    file2.write(my_num2.encode())

with open("new_file1.bin", "rb") as file1:
    number_lines = file1.read().decode()

with open("new_file2.bin", "rb") as file2:
    number_lines2 = file2.read().decode()

with open("new_file1.bin", "wb") as file1:
    file1.write(number_lines2.encode())

with open("new_file2.bin", "wb") as file2:
    file2.write(number_lines.encode())
