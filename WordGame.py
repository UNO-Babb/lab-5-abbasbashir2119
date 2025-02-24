import random

def in_word(letter, word):
    """
    Returns True if letter is found anywhere in the word (case-insensitive).
    """
    return letter.upper() in word.upper()

def in_spot(letter, word, spot):
    """
    Returns True if the letter at the given index (spot) in the word matches the letter (case-insensitive).
    """
    if 0 <= spot < len(word):
        return word[spot].upper() == letter.upper()
    return False

def rate_guess(guess, word):
    """
    Compares the guess with the target word and returns a string where:
    - Letters in the correct spot appear in uppercase.
    - Letters in the word but in the wrong spot appear in lowercase.
    - Letters not in the word are replaced by '*'.
    
    Assumes guess and word are of the same length.
    """
    result = ""
    for i in range(len(guess)):
        if in_spot(guess[i], word, i):
            result += guess[i].upper()
        elif in_word(guess[i], word):
            result += guess[i].lower()
        else:
            result += "*"
    return result

def main():
    # Attempt to read the words file
    try:
        with open("words.txt", "r") as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print("Error: words.txt not found!")
        return

    # Choose a random word as today's challenge.
    target_word = random.choice(words).strip()
    word_length = len(target_word)
    
    print("Welcome to the Word Game!")
    print(f"Guess the {word_length}-letter word. You have 6 attempts.\n")
    
    attempts = 6
    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: ").strip()
        
        # Ensure the guess has the correct length.
        if len(guess) != word_length:
            print(f"Your guess must be {word_length} letters long. Try again.\n")
            continue
        
        feedback = rate_guess(guess, target_word)
        print("Feedback:", feedback, "\n")
        
        if guess.upper() == target_word.upper():
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was: {target_word}")

if __name__ == '__main__':
    main()
