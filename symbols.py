def is_vowel(symbol):
    low_sym = symbol.lower()
    vowels = 'aeioquy'
    for i in vowels:
        return low_sym == i


print(is_vowel('a'))  # True
print(is_vowel('n'))  # False

