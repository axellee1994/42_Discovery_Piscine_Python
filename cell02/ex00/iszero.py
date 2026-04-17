#!/usr/bin/env python3

def main():
    number = int(input())
    try:
        if number == 0:
            print("This number is equal to zero")
        else:
            print("This number is different from zero")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()