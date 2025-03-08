from collections.abc import Iterable
# Учитывая строку, верните все возможные перестановки своих символов,
# отсортированные в алфавитном порядке.
from itertools import permutations
# Вариант кода с использованием библиотеки itertools
def string_permutations(s: str) -> Iterable[str]:
    unique_permutations = sorted(set("".join(p) for p in permutations(s)))
    return unique_permutations
# Permutations в Python — это функция из модуля itertools, которая
# возвращает все возможные перестановки итерируемого объекта с уникальным
# расположением элементов в итераторе


# Решение без itertools
def string_permutations(s: str) -> Iterable[str]:
    def permut(s):
        if len(s) == 1:
            return [s]

        permutations_list = []
        for i in range(len(s)):
            char = s[i]
            # Обрезаем строку и дальше идем рекурсивно по всей строке поэтапно отрезая первую букву
            permutind = s[:i] + s[i+1:]
            for mut in permut(permutind):
                permutations_list.append(char + mut)
        return permutations_list
    result = sorted(permut(s))
    return result


print("Example:")
print(list(string_permutations("abc")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
