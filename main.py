# Comment like a pro :)
# Author: Mr.Py
# Date: 2023-07-20

# Imported Library's
import random
import string

def generate_password():
    # Define the password length and the minimum required characters of each type
    length = 10
    min_uppercase = 2
    min_digits = 1
    min_special_symbols = 1

    # Define the character sets for each type of character
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_symbols = string.punctuation

    # Initialize the password string with empty values for each character type
    password = [random.choice(uppercase_letters) for _ in range(min_uppercase)]
    password += [random.choice(digits) for _ in range(min_digits)]
    password += [random.choice(special_symbols) for _ in range(min_special_symbols)]

    # Calculate the remaining characters for the password
    remaining_chars = length - (min_uppercase + min_digits + min_special_symbols)

    # Fill the remaining characters with a combination of uppercase letters, digits, and special symbols
    remaining_chars_pool = uppercase_letters + digits + special_symbols
    password += [random.choice(remaining_chars_pool) for _ in range(remaining_chars)]

    # Shuffle the password characters to ensure randomness
    random.shuffle(password)

    # Convert the list of characters into a string
    generated_password = ''.join(password)
    return generated_password

if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)



