firstNumber, secondNumber = int(input()), int(input())
enum = str(input())
def product(firstNumber,operation,secondNumber):
    if enum == '+':
        result = firstNumber + secondNumber
        return firstNumber,secondNumber,operation,result
    elif enum == '-':
        result = firstNumber - secondNumber
        return firstNumber,secondNumber,operation,result
    elif enum == '*':
        result = firstNumber * secondNumber
        return firstNumber,secondNumber,operation,result
    elif enum == '/':
        result = firstNumber / secondNumber
        return firstNumber,secondNumber,operation,result
print(product(firstNumber,enum,secondNumber))

