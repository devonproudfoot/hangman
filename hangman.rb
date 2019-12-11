class HangmanGame
	attr_reader :word, :correct_guesses

	def initialize(word, guesses=6)
		@word = word
		@remaining_guesses = 6
		@letters_guessed = []
		@correct_guesses = []
		word.each do |letter|
			@correct_guesses.push({ 'letter' : letter, 'guessed' : false })
		end
		play_game
	end

	private

	def play_game
		while remaining_guesses > 0
			display_board
			guess = prompt_guess

			if valid_guess?(guess)
				

			end 
		end
	end

	def guess_letter

	end

	def correct_guess?(letter)
		letter in @word ? true : false
	end

	def display_board
		board = []

		@correct_guesses.each do |letter_hash|
			if letter_hash['guessed']
				board.push(letter_hash['letter'])
			else
				board.push('_')
			end
		end

		puts board.join(' ')
	end

	def prompt_guess
		puts 'Enter your guess: '
		guess = gets.chomp.lower
	end

	def valid_guess?(guess)
		guess.length == 1 || guess =~ /[[:alpha:]]/ ? true : false
	end

end