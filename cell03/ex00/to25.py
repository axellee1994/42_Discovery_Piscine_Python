#!/usr/bin/env python3

def to25():
    number = int(input("Enter a number less than 25\n"))
    if number > 25:
        print("Error")
    else:
        for i in range(number, 26):
            print(f"Inside the loop, my variable is {i}")

def main():
    try:
        to25()
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()