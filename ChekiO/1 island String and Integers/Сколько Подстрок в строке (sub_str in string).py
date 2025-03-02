# Эта функция должна принимать основную строку и подстроение (подстроку) в качестве входов и
# возвращать количество случаев подстроения в основной строке.
# Это не должно быть чувствительным к случаям и может перекрываться.

def count_occurrences(main_str: str, sub_str: str) -> int:
    main_str, sub_str = main_str.lower(), sub_str.lower()
    count = 0
    i = 0
    while i <= len(main_str) - len(sub_str):
        if main_str[i:i + len(sub_str)] == sub_str:
            count += 1
            i += 1
        else:
            i += 1
    return count


print("Example:")
print(count_occurrences("appleappleapple", "appleapple"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1
