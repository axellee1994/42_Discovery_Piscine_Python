#!/usr/bin/env python3

import sys

def check_parameters():
    count = len(sys.argv) - 1
    print(f"Number of parameters: {count}")

def main():
    try:
        check_parameters()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()