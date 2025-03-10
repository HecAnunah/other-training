# def is_prime(number):
#     if number < 2:
#         return False
#     divider = 2 #Переводится как "Делитель"
#     while divider <= number / 2:
#         if number % divider == 0:
#             return False

#         divider += 1

#     return True

# print(is_prime(4))



#Иное решение:

number = int(input('Введите число ' ))
is_prime = True
for divider in range (2, number):
    if number % divider == 0:
        is_prime = False
        break
if is_prime:
    print('Число простое.')
else:
    print('Число составное.')
