# Эта функция должна взять список строк и определять самый длинный распространенный префикс
# среди всех строк. Если нет общего префикса, он должен вернуть пустую строку.

def longest_prefix(arr: list[str]) -> str:
    if not arr:  # Если список пустой, вернуть пустую строку
        return ""

    prefix = arr[0]  # Берем первую строку как начальный префикс

    for word in arr[1:]:  # Перебираем остальные слова
        while not word.startswith(prefix):  # Пока слово не начинается с prefix
            prefix = prefix[:-1]  # Обрезаем последний символ у prefix
            if not prefix:  # Если префикс стал пустым — выходим
                return ""

    return prefix


print("Example:")
print(repr(longest_prefix(["dog", "racecar", "car"])))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"
