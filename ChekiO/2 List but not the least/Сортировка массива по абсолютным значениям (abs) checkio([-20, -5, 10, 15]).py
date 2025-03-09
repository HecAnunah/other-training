# Давайте посмотрим на сортировку. Дан массив с особыми правилами.

# Массив (a list) содержит различные числа. Вам необходимо отсортировать их,
# но отсортировать на основе абсолютных значений в возрастающем порядке.
# Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим
# образом (-5, 10, 15, -20). Ваша функция должна возвращать список (list) или кортеж (tuple).

def checkio(values: list) -> list:
    new_list = sorted([abs(x) for x in values])
    minus_list = []

    for num in values:
        if num < 0:
            minus_list.append(abs(num))
    return [-x if x in minus_list else x for x in new_list]


print("Example:")
print(checkio([-20, -5, 10, 15]))
# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")
