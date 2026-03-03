from tm_add import AddTM
from tm_sub import SubTM
from tm_mul import MulTM
from tm_div import DivTM

class UniversalTuringMachine:
    def __init__(self):
        self.machines = {
            "ADD": AddTM(),
            "SUB": SubTM(),
            "MUL": MulTM(),
            "DIV": DivTM()
        }

    def run(self, opcode, a, b):
        if opcode not in self.machines:
            return "INVALID_OPERATION"
        tm = self.machines[opcode]
        return tm.run(a, b)
