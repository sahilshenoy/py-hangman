import random

# List of words for the game
words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape"]

# Function to select a random word from the list
def get_random_word():
    return random.choice(words)

# Function to initialize the game
def initialize_game():
    word = get_random_word()
    guessed_letters = []
    tries = 6
    return word, guessed_letters, tries

# Function to display the hangman
def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

# Function to update the guessed word
def update_guessed_word(word, guessed_letters):
    guessed_word = ""
    for letter in word:
        if letter in guessed_letters:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word

# Function to play the game
def play_hangman():
    print("Welcome to Hangman!")
    word, guessed_letters, tries = initialize_game()
    guessed_word = update_guessed_word(word, guessed_letters)

    while tries > 0:
        print(display_hangman(tries))
        print("Word:", guessed_word)

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            guessed_word = update_guessed_word(word, guessed_letters)
            if guessed_word == word:
                print("Congratulations! You guessed the word correctly:", word)
                break
            else:
                print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1
            if tries == 0:
                print(display_hangman(tries))
                print("Game over! You ran out of tries.")
                print("The word was:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thank you for playing Hangman!")

# Start the game
play_hangman()
