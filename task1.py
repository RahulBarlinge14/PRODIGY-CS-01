def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    message = input("Enter the message to encrypt/decrypt: ")
    shift_value = int(input("Enter the shift value: "))
    choice = input("Encrypt (E) or Decrypt (D)?: ").upper()
    
    if choice == 'E':
        encrypted_message = encrypt(message, shift_value)
        print("Encrypted message:", encrypted_message)
    elif choice == 'D':
        decrypted_message = decrypt(message, shift_value)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please choose either 'E' or 'D'.")

if __name__ == "__main__":
    main()
