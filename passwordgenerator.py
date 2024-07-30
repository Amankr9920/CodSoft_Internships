import random
import string

def generate_password(length):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine the character sets
    all_chars = lowercase + uppercase + digits + special_chars

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the password to avoid the first characters always being from the same set
    random.shuffle(password)

    # Join the password into a single string
    return ''.join(password)

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length (min 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "_main_": main() 