# Project 2: Random Password Generator
import random

# Define constants, set up variables, specify how to generate passwords
CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-_=+[]{}|;:,<.>/?"
password_list = []
password_length = int(input("Enter the number of characters you want your password to have: "))
number_of_passwords = int(input("Enter how many passwords you want generated: "))

# Generate a certain number of passwords with a specified amount of characters
for passwords in range(number_of_passwords):
    generated_password = ""
    for character in range(password_length):
        generated_password = generated_password + CHARACTERS[random.randint(0, 90)]
    password_list.append(generated_password)

# Print the passwords
for number, password in enumerate(password_list):
    print(str(number + 1) + ". " + password)