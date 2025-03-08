
#если мы возьмем 100 и поделим целочисленно на 4, то получим кол-во чисел в
# числе 100, которые можно поделить на 4

def count_divisible(n: int, k: int) -> int:
    return n // k


def count_divisible(n: int, k: int) -> int:
    count = 0
    number_list = [x for x in range(1, n + 1)]
    for num in number_list:
        if not num % k:
            count += 1
    return count



print("Example:")
print(count_divisible(2, 1))

# These "asserts" are used for self-checking
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3
assert count_divisible(20, 6) == 3
assert count_divisible(100, 10) == 10
assert count_divisible(200, 25) == 8
assert count_divisible(50, 7) == 7
assert count_divisible(60, 8) == 7
assert count_divisible(70, 9) == 7
