#Project 3: Caesar Cipher

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
finalString = ""

def cipherLoop():
    global currentLetter, finalString
    for letter in initialString:
                if letter == " ":
                    finalString = finalString + " "
                elif letters.find(letter) == -1:
                    continue
                else:
                    currentLetter = letter
                    if mode == 1:
                        addCipher()
                    elif mode == 2:
                        subtractCipher(key)
                    elif mode == 3:
                        subtractCipher(tries)

def convertCipher():
    global currentLetter, key, finalString, initialString
    initialString = str(input("Enter the string to convert: ")).upper()
    key = int(input("Enter the key for the Caesar Cipher (0-25): "))
    cipherLoop()
    print(finalString)

def addCipher():
    global finalString
    if int((letters.find(currentLetter)) + key) >= 25:
        finalString = finalString + str(letters[int(((letters.find(currentLetter)) + key) % 25) - 1])
    else:
        finalString = finalString + str(letters[int((letters.find(currentLetter)) + key) % 25])

def subtractCipher(modeType):
    global finalString
    if int((letters.find(currentLetter)) - modeType) < 0:
        finalString = finalString + str(letters[int(((letters.find(currentLetter)) - modeType) % 25) + 1])
    else:
        finalString = finalString + str(letters[int((letters.find(currentLetter)) - modeType) % 25])

print("Select an option:")
print("1. Encrypt a string.")
print("2. Decrypt a Caesar Cipher.")
print("3. Brute force a Caesar Cipher.")
mode = int(input("> "))

if mode == 1 or mode == 2:
    convertCipher()

elif mode == 3:
    initialString = str(input("Enter the Caesar Cipher to brute force: ")).upper()
    for tries in range(0,26):
        finalString = ""
        cipherLoop()
        print("Key " + str(tries) + ": " + finalString)
