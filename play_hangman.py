from getpass import getpass
from hangman import HangmanGame


def main():
  word_to_guess = getpass('Please enter a word for the opponent to guess: ')
  new_game = HangmanGame(word_to_guess)
  new_game.play_game()

if __name__ == '__main__':
  main()