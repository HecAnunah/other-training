# Функция RGB неполная. Завершите его так, чтобы передача десятичных значений
# RGB приводила к возврату шестнадцатеричного представления.
# Допустимые десятичные значения для RGB: 0–255.
# Любые значения, выходящие за пределы этого диапазона, должны быть округлены до
# ближайшего допустимого значения.
# Примечание.
# Ваш ответ всегда должен состоять из 6 символов, сокращение из 3 здесь не подойдет.
# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r,g,b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return "{:02X}{:02X}{:02X}".format(r,g,b)


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

test = rgb(255, 255, 255)
print(test)
