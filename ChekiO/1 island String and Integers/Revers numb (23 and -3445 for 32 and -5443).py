def reverse_digits(num: int) -> int:
    if num < 0:
        result = int(str(abs(num))[::-1])
        return -1 * result
    else:
        result = int(str(num)[::-1])
        return result

# Упрощенный код
def reverse_digits(num: int) -> int:
    sign = -1 if num < 0 else 1
    return sign * int(str(abs(num))[::-1])

print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789
