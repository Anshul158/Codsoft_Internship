import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "`~!@#$%^&*()"
    all_chars = letters + letters.upper() + numbers + symbols

    password = ""
    for _ in range(length):
        password += random.choice(all_chars)
    
    return password

print("Password Generator")
length = int(input("Enter desired password length : "))
if length <= 0:
    print("Length should be a positive number.")
else:
    password = generate_password(length)
    print("Generated Password:", password)

