def join_numbers_from_range(start, finish):
    result = ''
    i = start
    while i <= finish:
        result = str(i) + result
        i = i + 1
    return result


print(join_numbers_from_range(1, 3))
