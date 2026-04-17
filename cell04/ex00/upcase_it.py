#!/usr/bin/env python3

def upcase_it():
    s = input("Give me a word: ")
    print(s.upper())

def main():
    try:
        upcase_it()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()