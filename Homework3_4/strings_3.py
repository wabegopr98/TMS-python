"""Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
ваше имя."""

txt = "my name is name"
txt_new = txt.split()
your_name = input("Введите ваше имя")
txt2 = f"{txt_new[0]} {txt_new[1]} {txt_new[2]} {your_name}"
print(txt2)