

s ="Это пример строки с некоторым количеством слов"
print('1 --- ', s)
words = s.split()# Разбиваем строку на слова
print('2 --- ', words)
reversed_words = words[::-1]# Изменяем порядок слов на обратный
print('3 --- ', reversed_words)
reversed_s = ' '.join(reversed_words)# Объединяем слова обратно в строку
print('4 --- ',reversed_s)# Выводим результат
