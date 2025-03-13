# Сама по себе пешка является слабой фигурой, но мы можем использовать до
# восьми пешек для построения оборонительной стены. Стратегия оборонительной
# стены основывается на защите друг друга. Пешка защищена, если её клетка находится
# по ударом другой своей пешки. На игровом поле находятся только белые пешки.
# Вы должны разработать код, позволяющий определить сколько пешек защищены в этой позиции.

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]

def safe_pawns(pawns: set) -> int:
    def_count = 0
    for pawn in pawns:
        col, row = pawn[0], int(pawn[1])
        left_def = chr(ord(col) - 1) + str(row - 1)
        right_def = chr(ord(col) + 1) + str(row - 1)
        if left_def in pawns or right_def in pawns:
            def_count += 1
    return def_count


print("Example:")
print(safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}))
assert safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}) == 6
assert safe_pawns({"f4", "e5", "g4", "e4", "b4", "d4", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
