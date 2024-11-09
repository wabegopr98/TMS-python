"""Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”"""

spisok1 = ["Ivan", "Ivanou"]
spisok2 = " ".join(spisok1)

city = "Minsk"
country = "Belarus"

greeting = f"{"Привет,"}{spisok2 + "! "} {"Добро пожаловать в "}{city + " "}{country}"
print(greeting)
