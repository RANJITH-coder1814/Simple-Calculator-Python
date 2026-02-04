def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


print("=== Simple Calculator ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4): "))

if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
elif choice == 3:
    print("Result:", multiply(a, b))
elif choice == 4:
    print("Result:", divide(a, b))
else:
    print("Invalid Choice")
