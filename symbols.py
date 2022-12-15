def is_vowel(text):
    low_text = text.lower()
    vowels = 'aeioquy'
    vowels_count = 0
    index = 0
    while index < len(text):
        for i in vowels:
            if low_text[index] == i:
                vowels_count += 1
        return vowels_count


print(is_vowel('a'))  # True
print(is_vowel('n'))  # False

