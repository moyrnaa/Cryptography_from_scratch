# Just like encryption, but with negative steps. :) 
def decrypt_caesar(text, step):
    decrypted_text = []

    for char in text:
        if char.isupper():
            # Reverse shift for uppercase
            decrypted_char = chr((ord(char) - ord('A') - step) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        elif char.islower():
            # Reverse shift for lowercase
            decrypted_char = chr((ord(char) - ord('a') - step) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
        elif char.isdigit():
            # Reverse shift for numbers
            decrypted_char = str((int(char) - step) % 10)
            decrypted_text.append(decrypted_char)
        else:
            # Keep non alphabet/non number characters
            decrypted_text.append(char)

    return ''.join(decrypted_text)

encrypted_str = input("Enter encrypted string: ")
step = int(input("Enter the step (shift used for encryption): "))
decrypted_str = decrypt_caesar(encrypted_str, step)
print("Decrypted string:", decrypted_str)
