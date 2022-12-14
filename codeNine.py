# В переменной value хранится строковое представление числа.
# Получите модуль этого числа, используя функцию abs() и запишите его в ту же переменную value.
# Перед этим нужно привести строку к числу.

value = "-42"

# BEGIN (write your solution here)
value = str(abs(float(value)))
# END

print(value)
