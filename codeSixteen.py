# Task:
# С помощью слайсов, получите часть предложения, записанного в переменную text, c 5 по 16 символы включительно.
# Полученную подстроку обработайте методом .strip() и выведите на экран длину итоговой подстроки.
# Выполните эти операции подряд в цепочке без создания промежуточных переменных.

text = 'When \t\n you play a \t\n game of thrones you win or you die.'

# BEGIN (write your solution here)
slice_params = slice(5, 16)
print(len(text[slice_params].strip()))


# first function
def print_text():
    print('hi, pga')


print_text()
# END
