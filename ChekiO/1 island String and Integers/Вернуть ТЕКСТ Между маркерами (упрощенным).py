# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.

# Output: Строка.

# Пример:

# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert between_markers("What is [apple]", "[", "]") == "apple"
# assert between_markers("What is ><", ">", "<") == ""
# assert between_markers("[an apple]", "[", "]") == "an apple"


def between_markers(text: str, start: str, end: str) -> str:
    start_index = text.find(start) + len(start) if start in text else 0
    end_index = text.find(end) if end in text else len(text)
    return text[start_index:end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))
