import sys

class HangmanGame:


	def __init__(self, word_to_guess, guesses=6):
		self._word_to_guess = word_to_guess.lower()
		self._letters_status = self._create_letter_status()
		self._letters_guessed = []
		self._remaining_guesses = guesses


	def play_game(self):
		while self._remaining_guesses > 0:
			print('----------------------------------\n\n\n')
			print('You have guessed: {}\n'.format(self._letters_guessed))
			self._display_board()
			self._is_winner()
			self._guess_letter()
		self._handle_losses()


	def set_new_word(self, new_word):
		self.word = new_word


	def _is_winner(self):
		winner = True
		for letter in self._letters_status:
			if not letter['status']:
				winner = False
				break
		if winner:
			self._handle_wins()


	def _handle_wins(self):
		print('Congrats you have won!')
		sys.exit()


	def _handle_losses(self):
		print('Sorry, you lose! The answer was {}'.format(self._word_to_guess))
		sys.exit()


	def _guess_letter(self):
		letter = input('Please guess a letter: ').lower()

		if self._incorrect_value(letter):
			print('{} is not a letter!'.format(letter))
		elif letter in self._letters_guessed:
			print('You already guessed {}!'.format(letter))
		elif letter in self._word_to_guess:
			self._add_to_board(letter)
			self._letters_guessed.append(letter)
		else:
			self._remaining_guesses -= 1
			self._letters_guessed.append(letter)
			print('Wrong! You have {} guesses left!'.format(self._remaining_guesses))


	def _add_to_board(self, letter):
		for indx, character in enumerate(self._word_to_guess):
			if character == letter:
				self._letters_status[indx]['status'] = True


	def _incorrect_value(self, letter):
		if not letter.isalpha() or len(letter) >1:
			return True
		else:
			return False


	def _display_board(self):
		board = []

		for letter_dict in self._letters_status:
			letter = letter_dict['letter']
			if letter_dict['status']:
				board.append(letter)
			else:
				board.append('_')
		print(' '.join(board))


	def _create_letter_status(self):
		letters_status = []
		for letter in self._word_to_guess:
			letters_status.append({'letter': letter, 'status' : False})
		return letters_status