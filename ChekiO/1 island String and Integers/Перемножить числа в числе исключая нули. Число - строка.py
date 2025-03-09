# Дано положительное целое число. Вам необходимо подсчитать произведение
# всех цифр в этом числе, за исключением нулей.

# Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

def checkio(number: int) -> int:
    result = 1
    for num in map(int, str(number)):
        if int(num) != 0:
            result *= num

    return result


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
