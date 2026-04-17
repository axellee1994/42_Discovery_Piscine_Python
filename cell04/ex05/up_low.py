#!/usr/bin/env python3

def up_low():
    text = input()
    case_change = text.swapcase()
    print(case_change)

def main():
    try:
        up_low()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()