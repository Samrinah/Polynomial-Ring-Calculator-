def decimal_to_binary(n):
    n = int(n)
    if n == 0:
        return "0"

    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return ''.join(bits[::-1])


def binary_to_decimal(b):
    value = 0
    for bit in b:
        value = value * 2 + (bit == '1')
    return value
