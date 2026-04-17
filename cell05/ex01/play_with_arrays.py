#!/usr/bin/env python3

def play_with_arrays():
    
    # Option for dynamic array
    # array = input("Enter a list of integers separated by spaces: ")
    # array = [int(x) for x in array.split()]

    array = [2, 8, 9, 48, 8, 22,-12,2]
    print(array)

    new_array = [x + 2 for x in array]
    print(new_array)

def main():
    try:
        play_with_arrays()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()