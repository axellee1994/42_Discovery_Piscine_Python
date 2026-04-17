#!/usr/bin/env python3

def multiply():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    result = first_number * second_number

    print(f"{first_number} x {second_number} = {result}")
    
    if result < 0:
        print("The result is negative.")
    elif result == 0:
        print("The result is positive and negative.")
    else:
        print("The result is positive.")

def main():
    multiply()

if __name__ == "__main__":
    main()