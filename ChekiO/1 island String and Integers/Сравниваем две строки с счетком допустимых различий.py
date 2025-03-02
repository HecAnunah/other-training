# Учитывая две строки и допустимое количество различий в символах, определите,
# можно ли считать строки приблизительно равными.


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    lenn = min(len(str1), len(str2))
    count = 0
    for i in range(lenn):
        if str1[i] != str2[i]:
            count += 1
    count += abs(len(str1) - len(str2)) # Добавляем разницу в длине строк
    return count <= threshold

print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False
