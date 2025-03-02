import speech_recognition as sr
import os

# Определяем путь для сохранения файла
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "recognized_text.txt")

def record_and_save():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")
        recognizer.adjust_for_ambient_noise(source)  # Убираем шумы
        audio = recognizer.listen(source)

    try:
        # Распознаем голос (по умолчанию Google Web Speech API)
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", text)

        # Сохраняем текст в файл на рабочий стол
        with open(desktop_path, "w", encoding="utf-8-sig") as file:
            file.write(text)

        print(f"Текст сохранен в: {desktop_path}")

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError:
        print("Ошибка при подключении к сервису распознавания")

# Запускаем функцию
record_and_save()

