# ==========================================
# COS202 Mathematical Calculator (MC)
# Author: David Oseni
# ==========================================

def calculator():
    print("=" * 40)
    print("     MATHEMATICAL CALCULATOR (MC)")
    print("=" * 40)

    while True:
        print("\nChoose an operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Floor Division (//)")
        print("6. Exponent (^)")
        print("7. Modulus (%)")
        print("8. Clear (C)")
        print("9. OFF")

        choice = input("Enter your choice (1-9): ")

        if choice == "9":
            print("Calculator OFF. Goodbye!")
            break

        if choice == "8":
            print("\n" * 50)
            continue

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result =", num1 + num2)

            elif choice == "2":
                print("Result =", num1 - num2)

            elif choice == "3":
                print("Result =", num1 * num2)

            elif choice == "4":
                if num2 != 0:
                    print("Result =", num1 / num2)
                else:
                    print("Error! Division by zero.")

            elif choice == "5":
                if num2 != 0:
                    print("Result =", num1 // num2)
                else:
                    print("Error! Division by zero.")

            elif choice == "6":
                print("Result =", num1 ** num2)

            elif choice == "7":
                if num2 != 0:
                    print("Result =", num1 % num2)
                else:
                    print("Error! Division by zero.")
        else:
            print("Invalid choice!")

calculator()
