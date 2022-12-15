# Реализуйте функцию count_vowels(), которая принимает строку, считает и возвращает количество гласных букв в ней.
# Для проверки, является ли буква гласной, импортируйте и используйте функцию is_vowel() из модуля symbols.py.
from symbols import is_vowel

print(is_vowel('a'))  # True
print(is_vowel('n'))  # False

print(count_vowels('One'))  # 2
print(count_vowels('London is the capital of Great Britain'))  # 13