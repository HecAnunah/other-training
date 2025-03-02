# Учитывая строковые представления двух целых чисел, верните строковое представление суммы этих целых чисел.
# Например: Sumstrings ('1', '2') // => '3'
# Строковое представление целого числа не будет содержать символов, кроме десяти цифр «0» до «9».
# Python: Ваше решение должно работать с огромными числами (около цифр MILION), преобразование в INT не будет работать.


def sum_strings(x, y):
    if not x: x = '0'
    if not y: y = '0'

    i, j = len(x) - 1, len(y) - 1
    carry = 0 # перенос ( если числа 9+9 то перенос 1)
    result = []

    while i >= 0 or j >= 0 or carry:
        digit_x = int(x[i]) if i >= 0 else 0
        digit_y = int(y[j]) if j >= 0 else 0

        total = digit_x + digit_y + carry
        carry = total // 10
        result.append(str(total % 10))

        i -= 1
        j -= 1
    result = result[::-1]
    if result[0] == '0' and len(result) > 1:
        result.pop(0)
    return ''.join(result)


test = sum_strings("123", "456")
print(test)
