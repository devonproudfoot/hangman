import sys
from getpass import getpass

class HangmanGame:
  letters_guessed = []
  remaining_guesses = 6
  
  def __init__(self, word_to_guess):
    self.word_to_guess = word_to_guess
    self.guessed_letters = []
    for letter in self.word_to_guess:
      self.guessed_letters.append({'letter': letter, 'status' : False})
    self.play_game()
    
  def play_game(self):
    while self.remaining_guesses > 0:
      print('You have guessed: {}\n'.format(self.letters_guessed))
      self.display_board()
      self.is_winner()
      self.guess_letter()
      print('\n- - - - - - - - - - - - - - - - - - - -')
    print('Sorry, you lose! The answer was {}'.format(self.word_to_guess))
    sys.exit()

  def is_winner(self):
    winner = True
    for letter in self.guessed_letters:
      if not letter['status']:
        winner = False
        break
    if winner:
      print('Congrats you have won!')
      sys.exit()
    else:
      return False

  def guess_letter(self):
    letter = input('Please guess a letter: ').lower()

    if self.incorrect_value(letter):
      print('{} is not a letter!'.format(letter))
    elif letter in self.letters_guessed:
      print('You already guessed {}!'.format(letter))
    elif letter in word_to_guess:
      self.add_to_board(letter)
      self.letters_guessed.append(letter)
    else:
      self.remaining_guesses -= 1
      self.letters_guessed.append(letter)
      print('Wrong! You have {} guesses left!'.format(self.remaining_guesses))

  def add_to_board(self, letter):
    for indx, character in enumerate(self.word_to_guess):
      if character == letter:
        self.guessed_letters[indx]['status'] = True

  def incorrect_value(self, letter):
    if not letter.isalpha() or len(letter) > 1:
      return True
    else:
      return False

  def display_board(self):
    board = []

    for letter_dict in self.guessed_letters:
      letter = letter_dict['letter']
      if letter_dict['status']:
        board.append(letter)
      else:
        board.append('_')
    print(' '.join(board))

if __name__ == "__main__":
  word_to_guess = getpass('Please enter a word for the opponent to guess: ')
  new_game = HangmanGame(word_to_guess)
