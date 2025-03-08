from datetime import datetime
# Эта функция должна принимать строку даты в формате dd/mm/yyyy и
# преобразовать ее в формат yyyy-mm-dd. Если ввод не находится в правильном формате,
# функция должна вернуть сообщение об ошибке «Ошибка: неверная дата».

def convert_date(date: str) -> str:
    try:
    # Считаем части:
        parts = date.split('/')
        if len(parts) != 3:
            return 'Error: Invalid date.'

    # Создаем переменные
        dd, mm, yyyy = parts

    # Все ли числа:
        if not (dd.isdigit() and mm.isdigit() and yyyy.isdigit()):
            return 'Error: Invalid date.'

    # Проверка на высокостный год:
        dd, mm, yyyy = int(dd), int(mm), int(yyyy)
        datetime(yyyy, mm, dd)

        return f'{yyyy:04d}-{mm:02d}-{dd:02d}'

    except ValueError:
        return 'Error: Invalid date.'



print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")
