def sumatoria(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return print(num1 + num2)
    else:
        raise TypeError("different input type")