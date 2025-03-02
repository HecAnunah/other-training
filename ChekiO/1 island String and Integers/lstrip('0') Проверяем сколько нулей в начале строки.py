def beginning_zeros(a: str) -> int:
    return len(a) - len(a.lstrip('0'))


print("Example:")
print(beginning_zeros("001"))
