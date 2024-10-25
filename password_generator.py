# password_generator.py
import random
import string

def password_generator():
    print("\n--- Password Generator ---")
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")
