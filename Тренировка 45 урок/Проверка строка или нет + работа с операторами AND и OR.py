def string_or_not(string):
    return isinstance(string, str) and 'yes' or 'no'

print(string_or_not('yea'))

# проверяет является ли переданный параметр строкой.
# Если да, то возвращается строка yes, иначе no.
