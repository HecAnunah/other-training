def translation(text: str) -> str:
    result = []
    vowels = "aeiouy"  # Гласные буквы
    i = 0

    while i < len(text):
        result.append(text[i])  # Добавляем текущую букву

        if text[i] in vowels:
            i += 3  # Пропускаем 2 лишние буквы (гласные пишутся 3 раза)
        elif text[i] == ' ':
            i += 1
        else:
            i += 2  # Пропускаем 1 лишнюю букву (согласные идут парами)

    return "".join(result)



print("Example:")
print(translation("hoooowe yyyooouuu duoooiiine"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"
