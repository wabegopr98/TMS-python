"""Необходимо составить список чисел которые указывают на длину слов в строке:
sentence = "thequick brown box jumps over the lazy dog", но только если слово не
"the" c обработкой исключений"""

try:
    sentence = "thequick brown box jumps over the lazy dog"
    ord_sentence = sentence.split()
    number_sentence = [len(word) for word in ord_sentence]
    print(number_sentence)
    for word in ord_sentence:
        word.startswith("the")

except:
    print("Найдено слово начинающееся на the")