# password_generator.py
import random
import string

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("No character types selected. Cannot generate password.")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def password_generator():
    print("\n--- Password Generator ---")
    mode = input("Choose mode: (1) Default (8 characters) (2) Manual: ")
    
    if mode == "1":
        # Default mode: 8-character password with letters, numbers, and special characters
        password = generate_password()
        print(f"Generated password (default mode): {password}")
    elif mode == "2":
        # Manual mode
        try:
            length = int(input("Enter password length: "))
        except ValueError:
            print("Invalid input for length. Please enter a number.")
            return
        
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        if use_letters:
            letter_case = input("Choose letter case (upper/lower/both): ").lower()
            use_upper = letter_case in ("upper", "both")
            use_lower = letter_case in ("lower", "both")
        else:
            use_upper = use_lower = False
        
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        if password:
            print(f"Generated password (manual mode): {password}")
    else:
        print("Invalid choice. Please select 1 for Default mode or 2 for Manual mode.")
