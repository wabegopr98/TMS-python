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

            if int(symbol) % 2 != 0:
                b+=symbol

            if a:
                with open("even_numbers", "w") as file2:
                    file2.write(str(a))
            if b:
                with open("odd_numbers", "w") as file3:
                    file3.write(str(b))

