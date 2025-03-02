def valid_braces(string):
    open_braces = {"(": 0, "[": 0, "{": 0}
    close_braces = {")": 0, "]": 0, "}": 0}

    for char in string:
        if char in open_braces:
            open_braces[char] += 1
        elif char in close_braces:
            close_braces[char] += 1
        else:
            continue

    if (open_braces["("] == close_braces[")"] and
        open_braces["["] == close_braces["]"] and
        open_braces["{"] == close_braces["}"]):
        return True
    else:
        return False

test = valid_braces(')()(')
print(test)
