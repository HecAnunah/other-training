from typing import Counter


def checkio(text: str) -> str:
    sym_count = Counter(sym for sym in text.lower() if sym.isalpha())
    return max(sym_count, key=sym_count.get)



print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
