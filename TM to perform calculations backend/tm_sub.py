from utils import strip_leading_zeros, compare_binary
from tm_add import TMTrace

class SubTM:
    def run(self, a, b):
        if compare_binary(a, b) < 0:
            return "ERROR_NEGATIVE"

        a = list(a)
        b = list(b)

        borrow = 0
        result = []
        tracer = TMTrace()

        while a:
            tracer.log("READ", a, b, result, len(a))

            x = int(a.pop())
            y = int(b.pop()) if b else 0

            diff = x - y - borrow

            if diff == 0:
                result.append('0')
                borrow = 0
            elif diff == 1:
                result.append('1')
                borrow = 0
            elif diff == -1:
                result.append('1')
                borrow = 1
            elif diff == -2:
                result.append('0')
                borrow = 1

        tracer.log("HALT", a, b, result, 0)

        return strip_leading_zeros(''.join(result[::-1]))
