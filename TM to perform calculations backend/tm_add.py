from utils import strip_leading_zeros

class TMTrace:
    def log(self, state, a_tape, b_tape, result, head_pos):
        input_section = ''.join(a_tape) + '#' + ''.join(b_tape)
        output_section = ''.join(result[::-1])
        pointer = ' ' * head_pos + '^'
        print(f"State: {state}")
        print(f"[{input_section}] -> [{output_section}]")
        print(pointer)
        print()

class AddTM:
    def run(self, a, b):
        a, b = list(a), list(b)
        carry = '0'
        result = []
        state = "READ"
        tracer = TMTrace()

        while a or b or carry == '1':
            tracer.log(state, a, b, result, len(a))

            x = a.pop() if a else '0'
            y = b.pop() if b else '0'

            if x == y:
                result.append(carry)
                carry = x
            else:
                result.append('1' if carry == '0' else '0')

            state = "MOVE"

        tracer.log("HALT", a, b, result, 0)

        return strip_leading_zeros(''.join(result[::-1]))
