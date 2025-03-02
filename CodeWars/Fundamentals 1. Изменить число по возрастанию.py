# Ваша задача — создать функцию, которая может принимать любое неотрицательное целое число в
# качестве аргумента и возвращать его с цифрами в порядке убывания.
# По сути, переставьте цифры, чтобы получить максимально возможное число.

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    num_list = [int(i) for i in str(num)]
    num_list.sort(reverse=True)
    num = ''.join(map(str, num_list))
    num = int(num)
    return num

test = descending_order(13341)
print(test)


# TOP CodeWars
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
