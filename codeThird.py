# Реализуйте функцию filter_string().
# Она принимает на вход строку и символ и возвращает новую строку, в которой удалён переданный символ во всех его позициях.
# Если строка не содержит указанный символ, то она возвращается без изменений.

# Итоговая строка также не должна содержать начальные и концевые пробелы:


def filter_string(data, sym):
    new_str = ''
    for symbol in data:
        if symbol == sym.lower() or symbol == sym.upper():
            new_str = new_str
        else:
            new_str += symbol

    return new_str.strip()


text = 'If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'

print(filter_string(text, 'O'))  # 'If I lk frward I win

text = 'I look back if you are lost'

print(filter_string(text, 'w'))

print(filter_string(text, 'I'))
