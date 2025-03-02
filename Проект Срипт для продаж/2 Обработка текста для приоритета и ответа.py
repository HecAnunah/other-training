text = "Привет, Андрей! Нет, я не пойду гулять сегодня, У меня зачет."

priority_answers = {
    1: {"Нет, я не пойду": "В другой раз уже у меня не выйдет", "Привет": "Привет!"},
    2: {"У меня зачет": "А я вчера свой зачет сдал."}
}

# Список для хранения найденных ответов
responses = []

# Обрабатываем приоритеты от высшего к низшему
for priority in sorted(priority_answers.keys()):
    for key_phrase, response in priority_answers[priority].items():
        if key_phrase in text:
            responses.append(response)

# Выводим ответы
for res in responses:
    print(res)
