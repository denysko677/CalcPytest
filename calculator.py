def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "На нуль ділити не можна!"
    else:
        return x / y

def integer_divide(x, y):
    if y == 0:
        return "На нуль ділити не можна!"
    else:
        return x // y

def modulo(x, y):
    if y == 0:
        return "На нуль ділити не можна!"
    else:
        return x % y

print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Цілочисельне ділення")
print("6. Остача від цілочисельного ділення")

choice = input("Введіть номер операції (1/2/3/4/5/6): ")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if choice == '1':
    print("Результат:", add(num1, num2))
elif choice == '2':
    print("Результат:", subtract(num1, num2))
elif choice == '3':
    print("Результат:", multiply(num1, num2))
elif choice == '4':
    print("Результат:", divide(num1, num2))
elif choice == '5':
    print("Результат:", integer_divide(num1, num2))
elif choice == '6':
    print("Результат:", modulo(num1, num2))
else:
    print("Некоректний вибір операції")
