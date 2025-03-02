# Напишите функцию, которая принимает строку фигурных скобок и определяет,
# допустим ли порядок фигурных скобок. Он должен возвращать true, если строка действительна,
# и false, если она недействительна.
# Все входные строки будут непустыми и будут состоять только из круглых, квадратных и фигурных
# скобок: ()[]{}.
# Что считается валидным?
# Строка фигурных скобок считается допустимой, если всем фигурным скобкам соответствует
# правильная фигурная скобка.
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False


def valid_braces(string):
    stack = []  # Стек для отслеживания открывающих скобок
    pairs = {')': '(', '}': '{', ']': '['}  # Сопоставление закрывающих и открывающих скобок

    for char in string:
        if char in pairs.values():  # Если это открывающая скобка
            stack.append(char)
        elif char in pairs.keys():  # Если это закрывающая скобка
            # Проверяем, есть ли соответствие с верхним элементом стека
            if stack and stack[-1] == pairs[char]:
                stack.pop()  # Убираем соответствующую открывающую скобку из стека
            else:
                return False  # Если нет соответствия, строка недействительна

    return not stack  # Если стек пустой, строка валидна


def valid_braces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0



# def validBraces(s):
#   while '{}' in s or '()' in s or '[]' in s:
#       s=s.replace('{}','')
#       s=s.replace('[]','')
#       s=s.replace('()','')
#   return s==''





strings = "(())[]"
test = valid_braces(strings)
print(test)
