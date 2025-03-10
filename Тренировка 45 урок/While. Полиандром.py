
def is_palindrome(text):
    pointer1 = 0
    pointer2 = len(text) - 1
    print(pointer2)
    while pointer2 - pointer1 > 0:
        if text[pointer1] != text[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True

print(is_palindrome('asaasa'))

# Yasy variant
# def is_palindorme(text):
#     return text == text[::-1]
