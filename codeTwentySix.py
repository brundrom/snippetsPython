# Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке.
# Для этого нужно идти от верхней границы к нижней.
# То есть счётчик должен быть инициализирован максимальным значением, а в теле цикла его нужно уменьшать.
# По окончании работы функция должна вывести строку finished!.


def print_numbers(count):
    while count >= 0:
        if count == 0:
            print('finished!')
            return 0
        else:
            print(count)
            count -= 1


print_numbers(4)
# => 4
# => 3
# => 2
# => 1
# => finished!
