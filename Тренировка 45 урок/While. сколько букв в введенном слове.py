def f(text, char):
    if not isinstance(char, str):
        raise ('char NOT a STR')
    count = 0
    index = 0
    while index < len(text):
        if text[index].lower() == char.lower():
            count += 1
        index += 1
    return count


print(f('herl', 'h'))
