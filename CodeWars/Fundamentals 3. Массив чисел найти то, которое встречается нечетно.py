# В массиве целых чисел найдите то, которое встречается нечетное количество раз.
# Всегда будет только одно целое число, которое появляется нечетное количество раз.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

# from collections import Counter

# def find_odd(arr):
#     counts = Counter(arr)
#     for num, count in counts.items():
#         if count % 2 != 0:  # Проверяем, если число встречается нечетное количество раз
#             return num

# array = [1, 1, 7]
# print(find_odd(array))

                                            # Решение через XOR:
def find_odd(arr):
    result = 0
    for num in arr:
        result ^= num  # Используем XOR
    return result

array = [1, 2, 2, 1, 3, 3, 3] #  - - 0 - - 0 - 3 по сути ХОR побитно 
                              # складывает значения и если они совпадают с числом i[bit] == i+1, 
                              # то их обнуляет. В цонке остается 1 нечетное число.
print(find_odd(array))  # Ожидаемый вывод: 3

#         Объяснение работы XOR:
# Операция XOR (^) обладает важным свойством:
# a ^ a = 0 (число само с собой даёт 0).
# a ^ 0 = a (число XOR с 0 остаётся неизменным).
# Если применить XOR ко всем элементам массива, то все числа,
# которые встречаются чётное количество раз, обнулятся.
# Останется только число, которое встречается нечетное количество раз.
