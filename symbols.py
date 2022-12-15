def is_vowel(symbol):
    low_sym = symbol.lower()
    vowels = 'aeiouyауоыиэяюёе'
    for i in vowels:
        if low_sym == i:
            return True
