def ccipher(text, step): #ccipher stands for caesar cipher ...
    encrypted_text = []




    for char in text:
        if char.isupper():
            # Shift uppercase characters
            encrypted_char = chr((ord(char) - ord('A') + step) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        elif char.islower():
            # Shift lowercase characters
            encrypted_char = chr((ord(char) - ord('a') + step) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
        elif char.isdigit():
            # Shift numeric characters
            encrypted_char = str((int(char) + step) % 10)  # Wrap around after 9
            encrypted_text.append(encrypted_char)
        else:
            # Leave non alphabet and non-numeric characters unchanged
            encrypted_text.append(char)


    return ''.join(encrypted_text)


str1 = input("Enter a string: ")
step = int(input("Enter the step (shift value): "))
encrypted_str = ccipher(str1, step)
print("Encrypted string:", encrypted_str)
