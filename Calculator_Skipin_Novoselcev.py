try: num1 = float(input("Число один")) 
op = input("Операция") 
num2 = float(input("Число два")) 
if op == "+": 
    result = num1 + num2 
elif op == "-": 
    result = num1 - num2 
elif op == "*": 
    result = num1 * num2 
elif op == "/": 
    result = num1 / num2 

print("Ответ:"result)
except ValueError:
    print("введите числа")