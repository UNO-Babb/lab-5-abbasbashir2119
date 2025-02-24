def caesar_cipher(text, key, decode=False):
    """
    Encrypts or decrypts a text using the Caesar cipher.
    
    Parameters:
        text (str): The input text to process.
        key (int): The number of positions to shift in the alphabet.
        decode (bool): If True, the function will decrypt the text.
                       Otherwise, it encrypts the text.
    
    Returns:
        str: The processed text after shifting.
    """
    # If decoding, reverse the shift.
    shift = -key if decode else key
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine the ASCII base for uppercase or lowercase.
            base = ord('A') if char.isupper() else ord('a')
            # Compute shifted position with wrap-around using modulo arithmetic.
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Non-alphabetical characters remain unchanged.
            result.append(char)
    
    return ''.join(result)


def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))
    
    encrypted = caesar_cipher(message, key)
    print("Encrypted:", encrypted)
    
    decrypted = caesar_cipher(encrypted, key, decode=True)
    print("Decrypted:", decrypted)


if __name__ == '__main__':
    main()
