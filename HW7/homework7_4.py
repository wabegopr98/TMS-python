"""Необходимо составить список чисел которые указывают на длину слов в строке:
sentence = "thequick brown box jumps over the lazy dog", но только если слово не
"the" c обработкой исключений"""
from logging import exception

sentence = "thequick brown box jumps over the lazy dog"
ord_sentence = sentence.split(" ")
number_sentence = []

for word in ord_sentence:
    try:
        if word == "the":

            raise Exception
        number_sentence.append(len(word))

    except:
        print("Найдено слово the")

print(number_sentence)
