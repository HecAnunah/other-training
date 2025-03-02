# Заполните решение так, чтобы он лишил весь текст, который следует за любым из наборов маркеров комментариев.
# Пример:

# apples, pears # and bananas
# grapes
# bananas !apples

# The output:

# apples, pears
# grapes
# bananas

# The code would be called like so:

# result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

def strip_comments(strng, markers):
    lines = strng.split('\n')  # Разделяем на строки
    result = []

    for line in lines:
        min_ind = len(line)

        for mark in markers:
            ind = line.find(mark)
            if ind != -1:
                min_ind = min(min_ind, ind)
        liness = line[:min_ind].rstrip()
        result.append(liness)

    return '\n'.join(result)


def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts] # Мы берём только первый элемент из результата split(), т.е. часть строки ДО маркера комментария.
    return '\n'.join(parts)

test = strip_comments('ab!sd\ngggg', ['!'])
print(test)
