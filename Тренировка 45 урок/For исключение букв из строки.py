def filter_string(text, char):
    result = ''
    for current_char in text:
        if current_char.lower() != char.lower():
            result += current_char
    return result.strip()

print(filter_string('asas', 'a'))


#Важно не забывать, что пременная Current_char берет
#знаки из коллекции Text поочередно и сравнивает их с Char. Если они не равны, то печатает этот
#знак, если равны – не печатает. Таким образом мы и исключаем какой-либо символ из Text.
