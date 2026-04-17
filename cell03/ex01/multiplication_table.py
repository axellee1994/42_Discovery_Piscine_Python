#!/usr/bin/env python3

def multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(0, 10):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    try:
        multiplication_table()
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()