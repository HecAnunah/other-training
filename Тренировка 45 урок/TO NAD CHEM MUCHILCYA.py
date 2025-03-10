
def chars_count(text, char):
    count = 0
    index = 0
    while index < len(text):# КОД НЕ РАБОТАЛ т.к. index стоял ЗА пределами While!
        if text[index].lower() == char.lower():
            count += 1
        index += 1
    return count
print(chars_count('heexleeeet', 'e'))
# Yasy variant
# def char_count(text, char):
#     return text.lower().count(char.lower())
# print(char_count('hexxlex', 'e'))
