#!/usr/bin/env python3

def age():
    age_input = int(input("Please tell me your age: "))
    print(f"You are {age_input} years old.")
    print(f"In 10 years, you will be {age_input + 10} years old.")
    print(f"In 20 years, you will be {age_input + 20} years old.")
    print(f"In 30 years, you will be {age_input + 30} years old.")

def main():
    try:
        age()
    except ValueError:
        print("Please enter a valid integer for your age.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()