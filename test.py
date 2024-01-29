num1 = 1
num2 = 0

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("soy el error")
        return "Operacion erronea"

print(divide(num1, num2))