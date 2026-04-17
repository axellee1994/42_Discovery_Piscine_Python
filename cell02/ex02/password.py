#!/usr/bin/env python3

def is_password():
    password = "Python is awesome"
    question = input()
    if question != password:
        print("ACCESS DENIED")
    else:
        print("ACCESS GRANTED")

def main():
    try:
        is_password()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()