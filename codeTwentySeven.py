# Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку и возвращает получившуюся строку:


def join_numbers_from_range(start, stop):
    line = ''
    while start <= stop:
        line += str(start)
        start += 1
    return line


print(join_numbers_from_range(1, 1))  # '1'
print(join_numbers_from_range(2, 3))  # '23'
print(join_numbers_from_range(5, 10)) # '5678910'