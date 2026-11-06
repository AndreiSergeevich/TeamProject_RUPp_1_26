def calculator():
    print("=== Простой калькулятор ===")
    print("Операции: +, -, *, /")
    
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректное число!")
        return
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль!")
            return
        result = num1 / num2
    else:
        print("Ошибка: неизвестная операция!")
        return
    
    print(f"Результат: {num1} {operator} {num2} = {result}")

calculator()