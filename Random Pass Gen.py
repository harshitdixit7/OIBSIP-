import random
import string

def get_user_input(prompt, valid_range):
    while True:
        try:

            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(F"Please enter a value within the range {valid_range}.")
        except ValueError:
            print("Invalid Input")


def get_password_length():
    return get_user_input("Enter the desired password length: ", range(1, 101))


def get_character_types():
    print("Select character types to include in the password:")
    print("1. Letters")
    print("2. Numbers")
    print("3. Symbols")

    choices = []
    while True:
        choice = get_user_input("Enter the number corresponding to your choice (Enter 0 to end): ", range(0, 4))
        if choice == 0:
            if choices:
                break
            else:
                print("You must select at least one character type.")
        elif choice not in choices:
            choices.append(choice)
    
    return choices

def generate_password(length, char_types):
    character_sets = {
        1: string.ascii_letters,
        2: string.digits,
        3: string.punctuation
    }

    all_characters = ''.join(character_sets[choice] for choice in char_types)
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator")

    length = get_password_length()
    char_types = get_character_types()

    password = generate_password(length, char_types)

    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()