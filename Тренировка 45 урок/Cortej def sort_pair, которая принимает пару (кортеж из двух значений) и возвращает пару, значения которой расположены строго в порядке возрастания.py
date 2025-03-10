def sort_pair(pair):
    a, b, = pair
    if a <= b:
        return (a, b)
    else:
        return (b, a)

print(sort_pair((5, 1)))
