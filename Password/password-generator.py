import random
import string

print("=== Random Password Generator ===")


while True:
    try:
        length = int(input("Enter password length (min 6): "))
        if length < 6:
            print("Password length must be at least 6.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'


characters = ""

if use_letters:
    characters += string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if not characters:
    print("Error: You must select at least one character type.")
    exit()


password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)
