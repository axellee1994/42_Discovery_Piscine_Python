first_name = "Axel"
last_name = "Lee"
whole_name = first_name + " " + last_name

def main():
    try:
        if not first_name or not last_name:
            raise ValueError("Both first name and last name must be provided.")
        print(f"{whole_name}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()