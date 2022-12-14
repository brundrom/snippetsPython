# Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины.
# Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа:


def my_substring(text, count):
    i = 0
    new_str = ''
    while i < count:
        new_str += text[i]
        i += 1
    return new_str


string = 'If I look back I am lost'
print(my_substring(string, 1))  # => 'I'

print(my_substring(string, 7))  # => 'If I lo'