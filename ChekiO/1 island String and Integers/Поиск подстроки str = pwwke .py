# Учитывая строку, найдите длину самой длинной подстроки без повторяющихся символов.

def longest_substr(s: str) -> int:
    max_len = 0

    for i, sym in enumerate(s):
        result = [sym]
        for alph in s[i+1:]:
            if alph not in result:
                result.append(alph)
            else:
                break
        max_len = max(max_len, len(result))
    return max_len

# Поиск подстроки с использованием указателей
def longest_substr(s: str) -> int:
    max_len = 0
    left = 0  # Левый указатель (граница окна)
    unique_chars = set()

    for right in range(len(s)):  # Правый указатель
        while s[right] in unique_chars:  # Если повтор, двигаем левый указатель
            unique_chars.remove(s[left])
            left += 1

        unique_chars.add(s[right])
        max_len = max(max_len, right - left + 1)  # Обновляем максимальную длину

    return max_len



print("Example:")
print(longest_substr("pwwke"))
