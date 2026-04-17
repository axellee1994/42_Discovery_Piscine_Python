first_name = input("Hey, what's your first name? : ")
last_name = input("And your last name? : ")
whole_name = first_name + " " + last_name

def main():
    try:
        if not first_name or not last_name:
            raise ValueError("Both first name and last name must be provided.")
        print(f"Well, pleased to meet you, {whole_name}.")
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()
