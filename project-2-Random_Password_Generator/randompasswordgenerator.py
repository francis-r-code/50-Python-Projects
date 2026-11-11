#Project 2: Random Password Generator
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-_=+[]{}|;:,<.>/?"
passwordList = []
passwordLength = int(input("Enter the number of characters you want your password to have: "))
numberOfPasswords = int(input("Enter how many passwords you want generated: "))

for passwords in range(numberOfPasswords):
    generatedPassword = ""
    for character in range(passwordLength):
        generatedPassword = generatedPassword + characters[random.randint(0,90)]
    passwordList.append(generatedPassword)

for number, password in enumerate(passwordList):
    print(str(number + 1) + ". " + password)
