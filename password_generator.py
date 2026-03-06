import random
import string

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_characters) for i in range(length))

# Display password
print("Generated Password:", password)
