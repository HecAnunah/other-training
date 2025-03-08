# Совершенное число — это положительное целое число, которое равно сумме
# всех своих собственных делителей, исключая само себя.

# Например, 28 — это совершенное число, потому что его делители:
#     1, 2, 4, 7 и 14, и их сумма равна 28.

# def is_perfect(n: int) -> bool:
#     nod_sum = sum(div for div in range(1, n // 2 + 1) if n % div == 0)
#     return nod_sum == n


# Ускоренный вариант
def is_perfect(n: int) -> bool:
    nod_sum = 1  # 1 всегда делитель
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            nod_sum += div
            if div != n // div:  # Добавляем парный делитель
                nod_sum += n // div
    return nod_sum == n if n != 1 else False  # 1 не является совершенным числом


print("Example:")
print(is_perfect(28))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
