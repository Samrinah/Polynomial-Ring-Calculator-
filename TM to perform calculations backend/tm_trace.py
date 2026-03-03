from utils import strip_leading_zeros, compare_binary
from tm_trace import TMTrace

class SubTM:
    def run(self, a, b):
        if compare_binary(a, b) < 0:
            return "ERROR_NEGATIVE"

        a, b = list(a), list(b)
        borrow = '0'
        result = []
        tracer = TMTrace()
        state = "READ"

        while a:
            tape = list("".join(a) + "#" + "".join(b) + "->" + "".join(result[::-1]))
            tracer.log(state, tape, len(a))

            x = a.pop()
            y = b.pop() if b else '0'

            if borrow == '0':
                if x == y:
                    result.append('0')
                elif x == '1':
                    result.append('1')
                else:
                    result.append('1')
                    borrow = '1'
            else:
                if x == y:
                    result.append('1')
                elif x == '1':
                    result.append('0')
                    borrow = '0'
                else:
                    result.append('0')

            state = "MOVE"

        tape = list("#->" + "".join(result[::-1]))
        tracer.log("HALT", tape, 0)

        return strip_leading_zeros(''.join(result[::-1]))
