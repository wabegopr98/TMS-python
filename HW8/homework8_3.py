"""На взод подается некоторое количество(не больше сотни) разделенных пробелом целых чисел(каждое не меньше 0 и не больше 19)
Выведите их через пробел в порядке лексикографического возрастания названмй этих чисел в английском языке.
Т.е скажем числа 1,2,3 должны быть выведены в порядке 1,3,2 поскольку слово two встречается в словаре встречается позже
слова three, а слово three встречается позже слова one
number_names = {0: "zero", 1:"one", 2: "two", 3: 'three",
4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
9: "nine", 10: "ten", 11:"eleven", 12: "twenteen", 13:"thirteen",
14: "fourteen", 15: "fivteen", 16: "sixteen", 17: "seventeen",
18: "eighteen", 19: "nineteen"}"""

number_names = {
    0: 'zero', 1:'one', 2: 'two', 3: 'three',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
    9: 'nine', 10: 'ten', 11:'eleven', 12: 'twenteen', 13:'thirteen',
    14: 'fourteen', 15: 'fivteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen'
}

def sort_numbers(nums_str):
    nums = nums_str.split()
    nums.sort(key=lambda x: number_names[int(x)])
    return ' '.join(nums)


print(sort_numbers("9 4 7"))

