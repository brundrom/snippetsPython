# Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений) и возвращает пару,
# значения которой расположены строго в порядке возрастания.

# Пример:

# обратите внимание на скобки у аргумента функции


def sort_pair(cort):
    (one, two) = cort
    if one > two:
        return (two, one)
    else:
        return (one, two)


print(sort_pair((5, 1)))
print(sort_pair((2, 2)))
print(sort_pair((7, 8)))

