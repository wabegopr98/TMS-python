with open("float.txt", "r") as file1:
    number_lines = file1.readlines()

with open("float.txt", "w") as file1:
   for line in number_lines:
       line = line.split(", ")
       squared_nums = [round(float(x)**2, 2) for x in line]
       file1.writelines(str(squared_nums))