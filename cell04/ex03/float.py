#!/usr/bin/env python3

def check_number():
    num = input("Give me a number: ")
    if '.' in num:
        print("This number is a float")
    else:
        print("This number is an integer")

def main():
    try:
        check_number()
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()