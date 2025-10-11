
def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

while True:
    print("Select operation:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice in ['1', '2']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {sum(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")