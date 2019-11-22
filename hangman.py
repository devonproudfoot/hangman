import sys
from getpass import getpass

class HangmanGame:
  complete = False
  letters_guessed = []
  remaining_guesses = 6
  
  def __init__(self, word_to_guess):
    self.word_to_guess = word_to_guess
    self.guessed_letters = {}
    for letter in self.word_to_guess:
      self.guessed_letters[letter] = False
    
  def play_game(self):
    while self.remaining_guesses > 0:
      self.display_board()
      self.guess_letter()

  def guess_letter(self):
    letter = input('Please guess a letter: ').lower()
    if letter in self.letters_guessed:
      print('You already guessed {}!'.format(letter))
    elif letter in word_to_guess:
      self.letters_guessed.append(letter)
      self.guessed_letters[letter] = True
    else:
      self.remaining_guesses -= 1
      print('Wrong! You have {} guesses left!'.format(self.remaining_guesses))

  def display_board(self):
    board = []
    for letter, status in self.guessed_letters.items():
      print(letter)
      if status:
        board.append(letter)
      else:
        board.append('_')
    print(board)


if __name__ == "__main__":
  while True:
    response = input('Want to play a game of hangman? y/n ')
    if response == 'y' or response == 'Y':
      word_to_guess = getpass('Please enter a word for the opponent to guess: ')
      new_game = HangmanGame(word_to_guess)
      new_game.play_game()
    else:
      print('Ok, bye!')
      sys.exit()
