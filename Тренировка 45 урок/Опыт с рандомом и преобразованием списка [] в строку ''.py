#Создаем из набранной строки случайный набор символов (из тех что мы использовали в тексте).
# Идея появилась после вопроса о том, как создать свой пароль в Питон. + ''.join() преобразует список (в нашем случаи) в строку.
# Т.к. random.sample(x, y) создает список [].


import random

def rand (text):
    if len(text) < 8:
        return('Меньше 8 символов')
    else:
       return ''.join(random.sample(text, len(text)))


print(rand('AsyaAsyaevna'))
