# Мой друг берет последовательность всех чисел от 1 до N (где n> 0).
# В этой последовательности он выбирает два числа, A и B.
# Он говорит, что продукт A и B должен быть равен сумме всех чисел в последовательности, за исключением A и B.
# Учитывая номер N, не могли бы вы рассказать мне цифры, которые он исключил из последовательности?

# Функция принимает параметр: n (n всегда строго больше 0) и возвращает массив или строку (в зависимости от языка) формы:
# что есть несколько возможных (а, б).
# Функция возвращает пустой массив (или пустую строку), если не найдено возможных чисел, что докажет,
# что мой друг не сказал правду! (GO: В этом случае вернуть ноль).
# Примеры:
#     Removnb (26) должен вернуться [(15, 21), (21, 15)]] или
#     Removnb (26) должен вернуть {{15, 21}, {21, 15}} или
#     Removenb (26) должен вернуться [[15, 21], [21, 15]] или
#     Removnb (26) должен вернуть [{15, 21}, {21, 15}] или
#     Removnb (26) должен вернуть "15 21, 21 15"

def removNb(n):
    # Step 1: Calculate the total sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2
    result = []

    # Step 2: Iterate over all pairs (a, b)
    for a in range(1, n + 1):
        b = (total_sum - a) / (a + 1)
        if b.is_integer() and b <= n:
            result.append((a, int(b)))


    # Step 3: Return the result
    if result:
        return result
    else:
        return []

test = removNb(26)
print(test)
