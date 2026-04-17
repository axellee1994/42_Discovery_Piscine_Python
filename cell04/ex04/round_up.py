#!/usr/bin/env python3

import math

def round_up():
    num = float(input("Give me a number: "))
    rounded_num = math.ceil(num)
    print(rounded_num)

def main():
    try:
        round_up()
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()