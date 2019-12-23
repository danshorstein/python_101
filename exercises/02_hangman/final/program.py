# hangman! one word only!

# Import random choice module
from random import choice

# Create list of possible answers
ANSWERS = [
    'ball',
    'cat',
    'dog',
    'bicycle'
]

# Select a random answer and save to answer variable
answer = choice(ANSWERS)

# Set starting number of incorrect answers
incorrect_answers = 3

# Create initial answer display
answer_display = '_ ' * len(answer)

# Initialize empty list of previous letter guesses
previous_guesses = []

# Print welcome message
print(f'Welcome to hangman! Random word is {len(answer)} letters. Good luck!')

# Create game loop
while True:

    # Print game display
    print('\n' * 20)
    print(f'You have {incorrect_answers} incorrect guesses remaining.')
    print(answer_display)
    print()

    # Print previous guesses, if any
    if previous_guesses:
        print('Letters you have guessed: ' + ' '.join(previous_guesses))
    
    # Get guess input from user
    guess = (input('Guess a letter! '))

    # Deal with previous letters being guessed again
    if guess in previous_guesses:
        print('You already guessed {guess}! Try a new letter!')
        continue

    # Add new guess to list of previous guesses
    previous_guesses.append(guess)

    # Deal with guess not being in the answer, and with game over if all guesses are used
    if guess not in answer:
        input(f'Sorry, bad guess! {guess} is not in the solution! Hit enter to continue.')
        print()
        incorrect_answers -= 1
        if incorrect_answers == 0:
            print('Game over!')
            exit()
        continue

    # Update the answer display
    answer_display = ' '.join(list(answer))
    for letter in answer:
        if letter not in previous_guesses:
            answer_display = answer_display.replace(letter, '_')

    # Deal with user winning!
    if '_' not in answer_display:
        print('\n' * 20)
        print(answer_display)
        print()
        print('You win!')
        print(f'Answer is {answer}!')
        quit()