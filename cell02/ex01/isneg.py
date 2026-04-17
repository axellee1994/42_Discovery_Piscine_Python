#!/usr/bin/env python3

def is_negative():
    number = int(input())
    if number == 0:
        print("This number is both positive and negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is negative.")

def main():
    try:
        is_negative()
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()