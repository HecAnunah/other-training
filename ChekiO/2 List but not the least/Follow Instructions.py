def follow(instructions: str) -> tuple[int, int] | list[int]:
    x = 0
    y = 0
    for symb in instructions:
        if symb == 'f':
            x += 1
        elif symb == 'b':
            x -= 1
        elif symb == 'l':
            y -= 1
        elif symb == 'r':
            y += 1

    return (y, x)


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]