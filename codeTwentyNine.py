# Реализуйте функцию is_contains_char(), которая проверяет, содержит ли строка указанную букву.
# Регистр букв не важен. Функция принимает два параметра:

#    Строка
#    Буква для поиска

# И возвращает результат проверки – булево значение.


def is_contains_char(text, sym):
    i = 0
    result = False
    while i < len(text):
        if text[i] == sym.lower() or text[i] == sym.upper():
            result = True
        i += 1
    return result


print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
