def  get_hidden_card(credit_number, lenght, count_number=16):
    return '*' * (count_number - lenght) + credit_number[-lenght:]

print(get_hidden_card('2034399002125581', 4))


def  get_hidden_card(credit_number, lenght, stars=4):
    return '*' * stars + credit_number[-lenght:]

print(get_hidden_card('2034399002125581', 4))
