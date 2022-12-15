# Is palindrome?
def is_palindrome(text):
    if text == "":
        return True
    else:
        it_word = text.lower()
        it_reversed_word = ''
        word_length = len(it_word)
        while word_length > 0:
            it_reversed_word += it_word[word_length - 1]
            word_length -= 1
        return it_word == it_reversed_word


print(is_palindrome(''))  # True пустая строка тоже считается палиндромом
print(is_palindrome('radar')) # True
print(is_palindrome('a')) # True
print(is_palindrome('abs')) # False
print(is_palindrome('ишак ищет у тещи каши')) # True