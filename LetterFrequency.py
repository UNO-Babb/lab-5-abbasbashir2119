import os

def count_letters(message):
    """
    Count the frequency of each alphabetical character in the message.
    Non-letter characters are ignored.
    
    Returns:
        str: CSV-formatted string with a header row ("Letter,Frequency").
    """
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Initialize a list of 26 zeros (one for each letter)
    frequencies = [0] * 26
    
    # Convert the message to uppercase for uniformity.
    for char in message.upper():
        if char in alpha:
            index = alpha.index(char)
            frequencies[index] += 1
    
    # Build CSV data as a string (with a header)
    csv_data = "Letter,Frequency\n"
    for i in range(26):
        csv_data += f"{alpha[i]},{frequencies[i]}\n"
    
    return csv_data

def write_to_file(file_text, filename="frq.csv"):
    """
    Writes the provided text to a file with the given filename.
    The file is created in the same directory as this script.
    """
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    
    with open(file_path, "w") as file:
        file.write(file_text)
    
    print(f"CSV file has been written to: {file_path}")

def main():
    message = input("Enter a message: ")
    csv_output = count_letters(message)
    print("\nLetter Frequencies:\n")
    print(csv_output)
    write_to_file(csv_output)

if __name__ == '__main__':
    main()
