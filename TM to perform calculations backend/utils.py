def strip_leading_zeros(s):
    s = s.lstrip('0')
    return s if s else '0'


def compare_binary(a, b):
    a = strip_leading_zeros(a)
    b = strip_leading_zeros(b)

    if len(a) > len(b): return 1
    if len(a) < len(b): return -1
    if a > b: return 1
    if a < b: return -1
    return 0
