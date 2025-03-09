# Ваша функция должна создать список списков, который представляет собой
# двумерную сетку с заданным количеством строк и Col.
# Эта сетка должна содержать целые числа (int) от начала до начала + строк * Cols-1 в порядке
# возрастания, но элементы каждой строки с нечетным индексом должны быть перечислены в порядке
# убывания, так что при чтении в порядке возрастания числа зигзагу через двумерную сетку.

def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    result = []
    current = start
    for row in range(rows):
        res = list(range(current, current + cols))
        if row % 2:
            res.reverse()
        result.append(res)
        current += cols
    return result

print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
