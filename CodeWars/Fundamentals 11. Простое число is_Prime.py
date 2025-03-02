def is_prime(num):
    if num < 2:
        return False
    for divider in range(2, int(num ** 0.5) + 1): # Быстрый вариант кода
        if not num % divider:
            return False
    if is_prime:
        return True

test = is_prime(3)
print(test)
