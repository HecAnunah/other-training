                                                                         #get_range
#
# Данная функция должна для заданного положительного числа аргумента n возвращать список чисел от нуля до n, не включая
# само число n. Если при вызове было передано отрицательное число или ноль, функция должна возвращать пустой список
#
# >>> get_range(5)
# [0, 1, 2, 3, 4]

def get_range(number):
    if number == 0 or number < 0:
        return []
    result_range = [0] #Создаем список
    i = 1
    while i < number: # Перебираем числа до Number
        result_range.append(i) # Добавляем в список новое значение (не убирая старое)
        i = i + 1
    return result_range

test = get_range(5)
print(test)
