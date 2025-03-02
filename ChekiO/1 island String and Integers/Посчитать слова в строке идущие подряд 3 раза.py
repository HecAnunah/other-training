# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.


def checkio(words: str) -> bool:
    new_word = words.split()
    count = 0
    for word in new_word:
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print("Example:")
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

assert checkio('Hello World hello') == True
assert checkio('He is 123 man') == False
assert checkio('1 2 3 4') == False
assert checkio('bla bla bla bla') == True
assert checkio('Hi') == False
assert checkio('one two 3 four five 6 seven eight 9 ten eleven 12') == False
assert checkio('one two 3 four 5 six 7 eight 9 ten eleven 12') == False
assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True
