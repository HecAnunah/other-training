import random


# BEGIN (write your solution here)
def choice_from_range(text, start, finish):
    char_random = random.randint(start, finish)
    char_random_new = text[char_random]
    return char_random_new

print(choice_from_range('Absdef', 3, 5))
# END
