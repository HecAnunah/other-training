# основные переменные
greeting = 'Введите номер карты:'
numbers_bit_depth = 16  # установим разрядность номера карты
incorrect_input = 'Неверно.'  # сообщение - если ввели неправильно
stars_count = 4  # звездочки по 4шт


def input_number():  # ввод номера карты, проверка правильности ввода
    print(greeting)
    card_number = input()  # вводим номер карты
    card_number = card_number.replace(" ", "")  # убираем все пробелы в введенном номере
    if len(card_number) != numbers_bit_depth:  # контроль кол-ва символов ввода
        print(incorrect_input)  # сообщаем о неправильном вводе
        return input_number()  # все сначала: введите номер карты
    if card_number.isdigit():  # номер карты это цифры, иначе начнем все сначала
        return visibility(card_number)  # сколько видимых цифр вначале и в конце
    else:
        print(incorrect_input)  # сообщаем о неправильном вводе
        return input_number()  # все сначала: введите номер карты


def visibility(card_number):  # отображение номера карты
    visible_begin = card_number[:4]  # первые 4 цифры
    visible_end = card_number[-4:]  # последние  4 цифры
    print(f"{visible_begin} {'*' * stars_count} {'*' * stars_count} {visible_end}")  # итог + звездочки 2 раза


input_number()
