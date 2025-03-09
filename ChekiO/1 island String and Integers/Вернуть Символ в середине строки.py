def middle(text: str) -> str:
    lens = len(text) // 2
    return text[lens] if len(text) % 2 else text[lens-1: lens+1]


print("Example:")
print(middle("middle"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
