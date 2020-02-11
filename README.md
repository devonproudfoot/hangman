# OOP Python Hangman

## General

A Hangman game written in python, with object oriented programing!

## Installation

- Ensure that you have Python3 installed
- Clone the repository by running `git clone https://github.com/devonproudfoot/hangman.git`

## Playing Game
- Navigate to the repository in your terminal
- Running `python3 play_hangman.py` will set you up with a new game!

## Advanced Use
```python
from hangman import HangmanGame

# Create a game with the word 'hello'!
game = HangmanGame('hello')

# Change the word if you change your mind!
game.set_new_word('another')

# Start the fun with the play_game function!
game.play_game()

# Give yourself less or more chances to guess!
expert_level = HangmanGame('challenge', 1)
```