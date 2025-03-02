# В данной строке вам нужно проверить, идет ли один символ сразу за другим.
# Если так - вернуть истин, иначе - ложь.
# Если один из символов не в данном словом - ваша функция должна вернуть ложь.
# Если два ищущих символа одинаковы - ваша функция должна вернуть ложь.

def goes_after(word: str, first: str, second: str) -> bool:
    start = word.find(first)
    end = word.find(second)
    if (start != -1 and end != -1) and start - end == -1:
        return True
    return False


print("Example:")
print(goes_after("world", "w", "o"))

# Иное решение
def goes_after(word: str, first: str, second: str) -> bool:
    return f"{first}{second}" in word
