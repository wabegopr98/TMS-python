with open("new_file1.bin", "r") as file1:
    number_lines = file1.readlines()

with open("new_file2.bin", "r") as file2:
    number_lines2 = file2.readlines()

with open("new_file1.bin", "w") as file1:
    file1.writelines(number_lines2)

with open("new_file2.bin", "w") as file2:
    file2.writelines(number_lines)
