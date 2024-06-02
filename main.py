from calculatorlogo import logo


def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    print(logo)
    num1 = float(input("What the first number? :"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What the next number? :"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'yes' to continue with {answer}, or type 'no' to start a new calculation: ") == 'yes':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
