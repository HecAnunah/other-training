def my_substr(string, step):
    index = len(string)
    reversed_string = ''
    while index >= 0:
        current_char = string[:step:-1] #Приме того, как прочитать эту же функцию что и ниже но, с конца->начало (задом наперед).
        new_sub = reversed_string + current_char
        index = index - 1
        return new_sub
print(my_substr('If I look back I am lost', 6))




 #Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины.
 # Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа:

 #string = 'If I look back I am lost'
 #print(my_substr(string, 1))  # => 'I'
 #print(my_substr(string, 7))  # => 'If I lo'

def my_substr(string, step):
    index = len(string)
    reversed_string = ''
    while index >= 0:
        current_char = string[:step] # Решено так, как и хотел Хекслет, условия выше.
        new_sub = reversed_string + current_char
        index -= 1
    return new_sub


print(my_substr('If I look back I am lost', 7))
