# Project 3: Caesar Cipher

# Define variables and constants
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
final_string = ""


# Generate cipher based on mode specified
def cipher_loop():
    global current_letter, final_string
    for letter in initial_string:
        if letter == " ":
            final_string = final_string + " "
        elif LETTERS.find(letter) == -1:
            continue
        else:
            current_letter = letter
            if mode == 1:
                add_cipher()
            elif mode == 2:
                subtract_cipher(key)
            elif mode == 3:
                subtract_cipher(tries)


# Determine whether to encode or decode a string, specify cipher's key
def convert_cipher():
    global current_letter, key, final_string, initial_string
    initial_string = str(input("Enter the string to convert: ")).upper()
    key = int(input("Enter the key for the Caesar Cipher (0-25): "))
    cipher_loop()
    print(final_string)


# Encrypt a cipher
def add_cipher():
    global final_string
    if int((LETTERS.find(current_letter)) + key) >= 25:
        final_string = final_string + str(LETTERS[int(((LETTERS.find(current_letter)) + key) % 25) - 1])
    else:
        final_string = final_string + str(LETTERS[int((LETTERS.find(current_letter)) + key) % 25])


# Decrypt a cipher
def subtract_cipher(mode_type):
    global final_string
    if int((LETTERS.find(current_letter)) - mode_type) < 0:
        final_string = final_string + str(LETTERS[int(((LETTERS.find(current_letter)) - mode_type) % 25) + 1])
    else:
        final_string = final_string + str(LETTERS[int((LETTERS.find(current_letter)) - mode_type) % 25])


# Display options
print("Select an option:")
print("1. Encrypt a string.")
print("2. Decrypt a Caesar Cipher.")
print("3. Brute force a Caesar Cipher.")
mode = int(input("> "))

# Determine cipher mode
if mode == 1 or mode == 2:
    convert_cipher()
elif mode == 3:
    initial_string = str(input("Enter the Caesar Cipher to brute force: ")).upper()
    for tries in range(0, 26):
        final_string = ""
        cipher_loop()
        print("Key " + str(tries) + ": " + final_string)