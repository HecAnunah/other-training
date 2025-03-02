def first_word(text: str) -> str:
    word = ""
    for char in text:
        if char.isalpha() or char == "'":  # Разрешаем буквы и апостроф
            word += char
        elif word:  # Если слово уже начали собирать и встретили разделитель, прерываемся
            break
    return word


print("Example:")
print(first_word("Hel'lo world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"


#Другое решение
import re

def first_word(text: str) -> str:
    return re.findall(r"[a-zA-Z']+", text)[0] 
