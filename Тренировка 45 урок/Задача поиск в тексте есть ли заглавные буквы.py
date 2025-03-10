def  has_upper_case(text):
    text_lowers = text.lower()
    result = text != text_lowers
    return result

print(has_upper_case('Ghtr'))
