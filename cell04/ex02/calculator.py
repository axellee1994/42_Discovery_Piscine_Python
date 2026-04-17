#!/usr/bin/env python3

def calculator():
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "undefined (division by zero)"

    print("Thank you!")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

def main():
    try:
        calculator()
    except ValueError:
        print("Please enter valid integers for the numbers.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()