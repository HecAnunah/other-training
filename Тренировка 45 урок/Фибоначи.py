def fib(n):
    fib1 = 0                         #Задаем начальные условия
    fib2 = 1
    i = 0
    while i <= n - 2:
        fib_sum = fib1 + fib2                      # Основная формула расчета
        fib1 = fib2                                # Начальные условия для следующей цифры в цикле
        fib2 = fib_sum
        #Тут мы должны поменять местами фиб1 с фиб2 для того, что бы идти вперед по последовательности. К примеру: 0.1.1.2.3.5
        #фиб1=1 + фиб2=2 == 3. Дальше, для получения следующего числа (5) мы должны фиб1 сделать фиб2 (т.е. теперь фиб 1 != 1, а == 2)
        # в свою очередь Фиб2 теперь равняется предыдущему числу последовательности, т.е. sum=fib1+fib2(1+2=3) => фиб2 == 3.
        i = i + 1
    return fib2

print(fib())

#Числа Фибоначчи являются элементами числовой последовательности,
# где каждое последующее число образуется посредством суммирования двух предыдущих,
# например: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…
