def letter_multiply(text: str, simb: str, count: int) -> str:
    pr = text.replace(simb, simb * count)
    return pr


print(letter_multiply('python', 'p', 3))


# Делал во 2 раз
# BEGIN (write your solution here)
def letter_multiply(text: str, letter: str, count: int) -> str:
    return text.replace(letter, letter * count)
print(letter_multiply('python', 'y', 2))
# END
