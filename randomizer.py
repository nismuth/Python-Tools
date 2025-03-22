
import random

while True:
    words = []  # Set outside loops to reset whenever a new list is made
    while True:
        word = input("Enter a word (or type 'done' to finish): ")
        if word.lower() == "done":
            break
        words.append(word)  # Adds to words list

    if words:
        random_word = random.choice(words)
        print("\nRandomly selected word:", random_word)  # Print random word before prompt
    else:
        print("\nNo words were entered. Please try again.")

    exit_program = input("\nWould you like to try again? (yes/no): ").strip().lower()  # Input made default
    if exit_program != "yes":
        break
