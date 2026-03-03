from tm_add import AddTM
from tm_sub import SubTM
from utils import strip_leading_zeros, compare_binary

class DivTM:
    def run(self, a, b):
        if strip_leading_zeros(b) == '0':
            return "ERROR_DIV_ZERO"

        quotient = '0'
        remainder = a

        while compare_binary(remainder, b) >= 0:
            remainder = SubTM().run(remainder, b)
            quotient = AddTM().run(quotient, '1')

        return strip_leading_zeros(quotient), strip_leading_zeros(remainder)
