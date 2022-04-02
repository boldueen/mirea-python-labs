first_number = int(input("first: "))
second_number = int(input("second: "))
operation_sign = str(input("operation: "))


def calculate(sign):
    if (sign == "/" and second_number == 0):
        return "888888"

    calculator = {
        "+": first_number + second_number,
        "-": first_number - second_number,
        "*": first_number * second_number,
        "/": first_number / second_number
    }

    return calculator.get(sign, "888888")


print(calculate(operation_sign))
