def string_or_not(text):
    result = isinstance(text, str) and 'yes' or 'no'
    return result


print(string_or_not('Hexlet')) # yes

print(string_or_not(10))      # no

print(string_or_not(''))       # yes

print(string_or_not(False))    # no