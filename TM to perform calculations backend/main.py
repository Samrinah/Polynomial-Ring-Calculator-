from utm import UniversalTuringMachine
from nlp_ml import nlp_parse_ml as nlp_parse
from encoder import decimal_to_binary, binary_to_decimal

def main():
    print("\nUNIVERSAL TM CALCULATOR ")

    text = input("Enter: ")
    op, nums, is_binary = nlp_parse(text)

    if len(nums) != 2:
        print("Error: need exactly two numbers")
        return

    a, b = nums

    if is_binary:
        a_bin, b_bin = a, b
    else:
        a_bin = decimal_to_binary(a)
        b_bin = decimal_to_binary(b)

    utm = UniversalTuringMachine()
    result = utm.run(op, a_bin, b_bin)


    print("\ninputs: ")
    print("A:", a_bin)
    print("B:", b_bin)
    result = utm.run(op, a_bin, b_bin)

    if op == "DIV":
        q, r = result
        print("\nResult:")
        print("Quotient (bin):", q)
        print("Quotient (dec):", binary_to_decimal(q))
        print("Remainder (bin):", r)
        print("Remainder (dec):", binary_to_decimal(r))
    else:
        print("\nResult:")
        print("Binary:", result)
        print("Decimal:", binary_to_decimal(result))

if __name__ == "__main__":
    main()
