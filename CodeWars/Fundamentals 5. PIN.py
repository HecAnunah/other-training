# Банкоматы допускают использование 4- или 6-значных PIN-кодов,
# а PIN-коды не могут содержать ничего, кроме ровно 4 или ровно 6 цифр.

# Если функции передана действительная строка PIN-кода, верните true, иначе верните false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# def validate_pin(pin):
#     pin = str(pin)
#     if pin.isdigit():
#         if len(pin) == 6 or len(pin) == 4:
#             return True
#     return False


def validate_pin(pin):
    pin = str(pin) # добавил везде. Метод isdigit не работает с int - только строки.
    return len(pin) in (4, 6) and pin.isdigit()

test = validate_pin(6)
print(test)
