import tkinter as tk
from tkinter import messagebox
from translate import Translator

# Сопоставление клавиш между русской и английской раскладкой
eng_to_rus = str.maketrans(
    'qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
    'йцукенгшщзхъфывапролджэячсмитьбю.'
)
rus_to_eng = str.maketrans(
    'йцукенгшщзхъфывапролджэячсмитьбю.',
    'qwertyuiop[]asdfghjkl;\'zxcvbnm,./'
)

def is_russian(text):
    return any('а' <= c <= 'я' or c == 'ё' for c in text.lower())

def is_latin(text):
    return any('a' <= c <= 'z' for c in text.lower())

def fix_layout(text):
    if is_latin(text) and not is_russian(text):  # если текст на латинице
        fixed = text.translate(eng_to_rus)  # пробуем перевести с латиницы на кириллицу
        if is_russian(fixed):  # если результат стал русским текстом
            return fixed
    return text

def smart_translate(text):
    text = fix_layout(text)  # исправляем раскладку

    if is_russian(text):  # если текст на русском
        translator = Translator(from_lang='ru', to_lang='en')  # переводим на английский
    else:  # если текст на английском
        translator = Translator(from_lang='en', to_lang='ru')  # переводим на русский

    result = translator.translate(text)

    # Иногда библиотека возвращает результат в верхнем регистре, а нам нужен нормальный регистр
    return result.capitalize()

def translate_text(event=None):
    input_text = input_field.get("1.0", tk.END).strip()  # получаем текст из поля ввода
    if not input_text:
        messagebox.showwarning("Пустой ввод", "Введите текст для перевода.")
        return
    try:
        translated = smart_translate(input_text)  # выполняем перевод
        output_field.config(state='normal')  # включаем редактирование поля вывода
        output_field.delete("1.0", tk.END)  # очищаем вывод
        output_field.insert(tk.END, translated)  # вставляем результат перевода
        output_field.config(state='disabled')  # отключаем редактирование
    except Exception as e:
        messagebox.showerror("Ошибка перевода", str(e))  # если ошибка, выводим сообщение

def translate_from_english(event=None):
    input_text = input_field.get("1.0", tk.END).strip()  # получаем текст из поля ввода
    if not input_text:
        messagebox.showwarning("Пустой ввод", "Введите текст для перевода.")
        return
    try:
        # Переводим только с английского на русский без исправления раскладки
        translator = Translator(from_lang='en', to_lang='ru')
        translated = translator.translate(input_text)  # выполняем перевод
        output_field.config(state='normal')  # включаем редактирование поля вывода
        output_field.delete("1.0", tk.END)  # очищаем вывод
        output_field.insert(tk.END, translated)  # вставляем результат перевода
        output_field.config(state='disabled')  # отключаем редактирование
    except Exception as e:
        messagebox.showerror("Ошибка перевода", str(e))  # если ошибка, выводим сообщение

def show_context_menu(event):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)  # показываем контекстное меню
    finally:
        context_menu.grab_release()  # освобождаем контекст меню

def paste_text():
    input_field.insert(tk.INSERT, root.clipboard_get())  # вставляем скопированный текст

# GUI
root = tk.Tk()
root.title("Умный Переводчик")

tk.Label(root, text="Введите текст:").pack(pady=5)

input_field = tk.Text(root, width=60, height=5)  # поле ввода текста
input_field.pack(pady=5)
input_field.bind("<Return>", lambda event: (translate_text(), "break"))  # Enter = Перевести
input_field.bind("<Button-3>", show_context_menu)  # правый клик для контекстного меню

# Контекстное меню для вставки
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Вставить", command=paste_text)

# Кнопка для обычного перевода
translate_button = tk.Button(root, text="С русского на англ (с учётом раскладки)", command=translate_text)  # кнопка перевода
translate_button.pack(pady=5)

# Кнопка для перевода только с английского на русский
translate_english_button = tk.Button(root, text="С английского на русский", command=translate_from_english)
translate_english_button.pack(pady=5)

tk.Label(root, text="Перевод:").pack(pady=5)
output_field = tk.Text(root, width=60, height=5, state='disabled')  # поле для вывода перевода
output_field.pack(pady=5)

root.mainloop()
