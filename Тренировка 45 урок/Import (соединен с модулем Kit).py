from kit import show_language, say_hello, say_bye
# При импорте если в кит запущена одна из функций - ее работа будет впереди.
def print_kit():
    show_language()
    say_hello()
    say_bye()

print_kit()
