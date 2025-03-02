def replace_all(mainText: str, target: str, repl: str) -> str:
    return mainText.replace(target, repl)  # Заменяет все вхождения target на repl

print("Пример:")
print(replace_all("OpenAI", "AI", "Source"))  # Ожидаемый вывод: "OpenSource"

assert replace_all("OpenAI", "AI", "Source") == "OpenSource"
assert replace_all("Я люблю AI", "AI", "Машинное обучение") == "Я люблю Машинное обучение"
assert replace_all("банан", "на", "xy") == "baxyxy"
