from typing import Union


def calculator(num1: Union[int, float], num2: Union[int, float], operation: str) -> Union[int, float]:
    if operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
