from tm_add import AddTM
from utils import strip_leading_zeros

class MulTM:
    def run(self, a, b):
        result = '0'
        shift = 0

        for bit in b[::-1]:
            if bit == '1':
                temp = a + ('0' * shift)
                result = AddTM().run(result, temp)
            shift += 1

        return strip_leading_zeros(result)
