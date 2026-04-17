#!/usr/bin/env python3

import sys

def advanced_mult():
    i = 0
    while i <= 10:
        j = 0
        row = f"Table de {i}:"
        while j <= 10:
            row += f" {i * j}"
            j += 1
        print(row)
        i += 1

def main():
    try:
        if len(sys.argv) > 1:
            raise Exception
        advanced_mult()
    except Exception as e:
        print("none")

if __name__ == "__main__":
    main()
