# Массив массивов называется зазубренным, если его субражей имеют различную длину.
# Однако в определенных сценариях вам может потребоваться нормализовать зубчатый массив.
# Нормализация в этом контексте включает в себя преобразование в прямоугольную матрицу измерений n x m,
# где n представляет количество субаррей, а M представляет длину самого длинного субрай.
# Это преобразование достигается путем заполнения более коротких субаррей с указанным значением
# (принятым в качестве аргумента) до тех пор, пока они не соответствуют длине самого длинного субарра.

# [
# [1, 2, 3],
# [4],
# [5, 6, 7, 8]
# ]
# Вывод:
# [
# [1, 2, 3, None],
# [4, None, None, None],
# [5, 6, 7, 8]
# ]

massiv = [
[1, 2, 3],
[1],
[5, 6, 7, 8]
]

def normalize(massiv, fill_value=None):
    if massiv:
        max_len = max([len(sublist) for sublist in massiv])
        for lenght in massiv:
            corrent = max_len - len(lenght)
            lenght.extend([fill_value] * corrent)
        return massiv
    else:
        return []

from itertools import zip_longest
def normalize(arr, fill_value=None):
    return list(map(list, zip(*zip_longest(*arr, fillvalue=fill_value))))

def normalize(arr, fill_value=None):
    size = max(map(len,arr), default=0)
    return [ r + [fill_value]*(size-len(r)) for r in arr ]




test = normalize(massiv)
print(test)
