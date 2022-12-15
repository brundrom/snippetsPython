# Реализуйте функцию count_vowels(), которая принимает строку, считает и возвращает количество гласных букв в ней.
# Для проверки, является ли буква гласной, импортируйте и используйте функцию is_vowel() из модуля symbols.py.
from symbols import is_vowel


def count_vowels(text):
    low_text = text.lower()
    vowels_count = 0
    for i in low_text:
        if is_vowel(i):
            vowels_count += 1
    return vowels_count


print(count_vowels('One'))  # 2
print(count_vowels('London is the capital of Great Britain'))  # 13