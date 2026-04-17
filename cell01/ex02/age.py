first_age = 31
second_age = 42
my_age = first_age + second_age

def main():
    try:
        if not isinstance(first_age, int) or not isinstance(second_age, int):
            raise ValueError("Both ages must be integers.")
        print(f"{my_age}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()