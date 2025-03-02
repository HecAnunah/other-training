# Вам дан массив (длина которого не менее 3, но может быть очень большим),
# содержащий целые числа. Массив либо полностью состоит из нечетных целых чисел,
# либо полностью состоит из четных целых чисел, за исключением одного целого числа N.
# Напишите метод, который принимает массив в качестве аргумента и возвращает это «выброс» N.
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (единственное нечетное число)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (единственное четное число)


# def find_outlier(integers):
#     chet_list = []
#     nechet_list = []
#     for numb in integers:
#         if numb % 2 == 0:
#             chet_list.append(numb)
#         else:
#             nechet_list.append(numb)
#     if len(chet_list) > len(nechet_list):
#         return int(nechet_list[0])
#     else:
#         return int(chet_list[0])



# def find_outlier(integers):
#     evens = [x for x in integers if not x % 2]
#     odds = [x for x in integers if x % 2]
#     return evens[0] if len(evens) == 1 else odds[0]

# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]



def find_outlier(integers):
    return next(x for x in integers if x % 2 == (sum(n % 2 for n in integers) == 1))

test = find_outlier([160, 3, 1719, 19, 11, 13, -21])
print(test)

# 0 == 6 == False  => 0 == False => Верный ответ 160
# 1 == 6 == False  => 1 == False
# 1 == 6 == False  => 1 == False
# 1 == 6 == False  => 1 == False
# 1 == 6 == False  => 1 == False
# 1 == 6 == False  => 1 == False
# 1 == 6 == False  => 1 == False
