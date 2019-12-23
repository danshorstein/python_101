# hangman! one word only!

# Import random choice module
from random import choice

# Create list of possible answers
ANSWERS = [

]

# Select a random answer and save to answer variable
answer = ...

# Set starting number of incorrect answers
incorrect_answers = ...

# Create initial answer display
answer_display = ...

# Initialize empty list of previous letter guesses
previous_guesses = ...

# Print welcome message
print(...)

# Create game loop
while True:

    # Print game display
    ...

    # Print previous guesses, if any
    if previous_guesses:
        ...
    
    # Get guess input from user
    guess = ...

    # Deal with previous letters being guessed again
    if guess in previous_guesses:
        ...

    # Add new guess to list of previous guesses
    ...

    # Deal with guess not being in the answer, and with game over if all guesses are used
    if guess not in answer:
        ...

    # Update the answer display
    answer_display = ...
    for letter in answer:
        ...

    # Deal with user winning!
    ...