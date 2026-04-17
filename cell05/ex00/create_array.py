#!/usr/bin/env python3

def create_array():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    print(array)

def main():
    try:
        create_array()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()