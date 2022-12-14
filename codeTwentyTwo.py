# Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы. Функция должна вернуть булево значение:

# has_upper_case('')  # False
# has_upper_case('python')  # False

# has_upper_case('pyThon')  # True


def has_upper_case(text):
    lower_text = text.lower()
    return text != lower_text


print(has_upper_case('pyThon'))
