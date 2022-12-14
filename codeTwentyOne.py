# Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей в возрасте в виде The age difference is 11
# actual = get_age_difference(2001, 2018)
# print(actual)  # => The age difference is 17


def get_age_difference(year_past, year_present):
    result = year_present - year_past
    return 'The age difference is ' + str(abs(result))


actual = get_age_difference(2020, 2010)
print(actual)
