#!/usr/bin/env python3

def is_password():
    password = "Python is awesome"
    question = input()
    if question != password:
        print("ACCESS DENIED")
    else:
        print("ACCESS GRANTED")

def main():
    is_password()

if __name__ == "__main__":
    main()