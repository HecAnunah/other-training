#Реализуйте функцию has_char(). Она должна проверять, содержит ли строка указанную букву (вне зависимости от регистра).
# Функция принимает два параметра:

#Строка
#Буква для поиска
#И возвращает результат проверки – булево значение.



def has_char(string, char):
    i = 0
    char_up = char.upper()
    while i < len(string):
        if string[i].upper() == char_up:
            return True
        i += 1
    return False


print(has_char('hexslet', 'i'))

#Yeisy variant
def has_char(string, char):
    return char.upper() in string.upper()

print(has_char('fffgsd', 'x'))
