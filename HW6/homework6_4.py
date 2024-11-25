"""Даны 2 файла произвольного типа. Поменять местами их содержимое.
Файлы должны быть бинарными."""
import pickle

with open("new_file1.bin", "wb") as file1:
    my_num = "100000101 00010101"
    pickle.dump(my_num, file1)

with open("new_file2.bin", "wb") as file2:
    my_num2 = "00101010 11010101"
    pickle.dump(my_num2, file2)

with open("new_file1.bin", "rb") as file1:
    number_lines = pickle.load(file1)

with open("new_file2.bin", "rb") as file2:
    number_lines2 = pickle.load(file2)

with open("new_file1.bin", "wb") as file1:
    pickle.dump(number_lines2,file1)

with open("new_file2.bin", "wb") as file2:
    pickle.dump(number_lines, file2)
