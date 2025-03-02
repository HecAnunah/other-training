# Реализуйте функцию, которая складывает два числа и возвращает их сумму в двоичном виде.
# Преобразование может быть выполнено до или после добавления.
# Возвращаемое двоичное число должно быть строкой.
# Примеры:(Ввод1, Ввод2 --> Вывод (объяснение)))
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(a, b):
    return format(a + b, 'b')

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary(a,b):
    return '{0:b}'.format(a + b)


test = add_binary(1, 1)
print(test)
