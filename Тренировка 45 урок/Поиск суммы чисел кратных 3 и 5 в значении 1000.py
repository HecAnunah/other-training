summ = 0
for number in range(3, 1000):
    if number % 3 == 0 or number % 5 == 0:
        print(number)
        summ += number
print('Сумма', summ)
