# Учитывая строку, которая представляет заголовок столбца, который отображается в листе Excel,
# верните соответствующий номер столбца.
# Excel   Decimal
#     A   1
#    ..
#     Z   26

# Цифры 1- цифры закончились. 2- Номера «цифры» начинаются с
# двойной первой «цифры» и перейдите к двойному последнему:
# Excel   Decimal
#     A   1
#    ..
#     Z   26
#    AA   27
#    ..
#    AZ   52
#    BA   53
#    ..
#    BZ   78
#    CA   79
#    ..
#    ..
#    ZZ   702

def column_number(name: str) -> int:
    if not name:
        return 0
    return (ord(name[0]) - ord('A') + 1) * (26 ** (len(name) - 1)) + column_number(name[1:])
print("Example:")
print(column_number("AAA"))

# # These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701
