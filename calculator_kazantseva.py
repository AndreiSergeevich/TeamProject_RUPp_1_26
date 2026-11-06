def calculate(a, b, op):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Ошибка: деление на ноль!"
    }
    return operations.get(op, lambda x, y: "Неизвестная операция")(a, b)

def main():
    print("=== Калькулятор (для практической работы) ===")
    while True:
        try:
            a = float(input("Первое число: "))
            op = input("Операция (+, -, *, /): ").strip()
            b = float(input("Второе число: "))
            result = calculate(a, b, op)
            print(f"Результат: {result}\n")
        except ValueError:
            print("Ошибка: введите числа корректно.\n")
        
        again = input("Ещё раз? (да/нет): ").strip().lower()
        if again not in ('да', 'д', 'yes', 'y'):
            print("Завершение работы.")
            break

if __name__ == "__main__":
    main()
