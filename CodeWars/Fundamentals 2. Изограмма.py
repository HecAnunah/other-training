# Изограмма – это слово, в котором нет повторяющихся букв, как последовательных,
# так и непоследовательных. Реализуйте функцию, которая определяет, является ли строка,
# содержащая только буквы, изограммой. Предположим, что пустая строка является изограммой.
# Не обращайте внимания на регистр букв.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

def is_isogram(string):
    string = string.lower()
    for i in range(len(string) - 1):
        if string[i] in string[i + 1:]: # Проверяем, есть ли текущий символ в оставшейся части строки
            return False
    return True

test = is_isogram('AbSs')
print(test)

# Улучшенный вариант.

def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))  # Сравниваем длину строки и множества её символов

# Пример использования:
test = is_isogram('Dermatoglyphics')
print(test)
