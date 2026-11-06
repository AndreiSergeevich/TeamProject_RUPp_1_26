num1 = float(input("Введите первое число: "))  
num2 = float(input("Введите второе число: "))  
operation = input("Введите операцию (+, -, *, /): ")  

if operation == "+":  
    result = num1 + num2  
elif operation == "-":  
    result = num1 - num2  
elif operation == "*":  
    result = num1 * num2  
elif operation == "/":  
    if num2 != 0:  
        result = num1 / num2  
    else:  
        result = "Ошибка: Деление на ноль!"  
else:  
    result = "Неизвестная операция!"  
  
print(f"Результат: {result}")  