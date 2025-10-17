from calc import sum, subtract, multiply, divide

def menu():
    print("Select operation:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '0':
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {sum(a, b)}")
    elif choice == '2':
        print(f"The result is: {subtract(a, b)}")
    elif choice == '3':
        print(f"The result is: {multiply(a, b)}")
    elif choice == '4':
        print(f"The result is: {divide(a, b)}")
    else:
        print("Invalid choice. Please try again.")