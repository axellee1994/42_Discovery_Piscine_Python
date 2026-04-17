#!/usr/bin/env python3

def igotthat():
    command = input("What you gotta say? : ")
    while command != "STOP":
        command = input("I got that! Anything else? : ")

def main():
    try:
        igotthat()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()