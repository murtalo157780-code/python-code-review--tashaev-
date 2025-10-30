def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def main():
    while True:
        print("Выберите операцию: add, subtract, multiply, divide или exit для выхода")
        operation = input().strip().lower()
        
        if operation == 'exit':
            break
        
        try:
            print("Введите первое число:")
            a = float(input())
            print("Введите второе число:")
            b = float(input())
            
            if operation == 'add':
                result = add(a, b)
            elif operation == 'subtract':
                result = subtract(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'divide':
                result = divide(a, b)
            else:
                print("Неверная операция")
                continue
            
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if name == "main":
    main()
