
import random
import string


def generate_password(min_length, max_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    while True:
        target_length = random.randint(min_length, max_length)
        pwd = ""
        has_number = False
        has_special = False

        for _ in range(target_length):
            new_char = random.choice(characters)
            pwd += new_char
            if new_char in digits:
                has_number = True
            if new_char in special:
                has_special = True

        if ((not numbers or has_number) and
            (not special_characters or has_special)):
            return pwd


min_length = int(input("Enter the minimum length: "))
max_length = int(input("Enter the maximum length: "))
has_number = input("Do you want to have numbers? (y/n): ").lower() == "y"
has_special = input("Do you want to have special characters? (y/n): ").lower() == "y"

pwd = generate_password(min_length, max_length, has_number, has_special)
print("The password is: ", pwd)
