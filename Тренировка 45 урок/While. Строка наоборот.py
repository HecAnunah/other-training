def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        ###!! Current_char печатает с последнего Индекса в пустой строке т.е. [-1] Это у нас буква 's'
        # а дальше мы идем по порядку с конца. Индекс нужен (index -= 1) для того, что бы печатались буквы с конца и к началу (current char дает только
        # 1 букву).
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string

print(reverse_string('Game Of Thrones'))
