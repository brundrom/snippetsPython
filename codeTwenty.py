# Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
# строку, offset — число символов, на которое нужно обрезать строку слева и repetitions — количество раз, сколько ее нужно повторить, и возращает получившуюся строку.
# Число символов для среза по умолчанию равно 0, а количество повторений по умолчанию 1.

text = 'python'


def trim_and_repeat(text, offset=0, repetitions=1):
    slice_params = slice(offset, 6)
    result = text[slice_params]
    result = result * repetitions
    return result


print(trim_and_repeat(text, offset=3, repetitions=2))  # honhon
print(trim_and_repeat(text, repetitions=3))  # pythonpythonpython
print(trim_and_repeat(text))  # python