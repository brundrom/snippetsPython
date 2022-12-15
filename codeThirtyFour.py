# Реализуйте функцию choice_from_range(), которая принимает строку-набор и выбирает случайный символ по индексу из ограниченного диапазона.
import random
# Аргументы функции:
# строка-набор
# начальный индекс диапазона
# конечный индекс диапазона


def choice_from_range(text, start, finish):
    edited_text = text[start:finish+1]
    return random.choice(edited_text)


text = "abcdef"
print(choice_from_range(text, 3, 5))  # d
print(choice_from_range(text, 3, 5))  # f
print(choice_from_range(text, 3, 5))  # e