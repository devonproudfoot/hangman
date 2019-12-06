class HangmanGame
	attr_reader :word

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
			guess = prompt_guess

		end
	end

	def correct_guess?(letter)
		letter in @word ? true : false
	end

	def prompt_guess
		puts 'Enter your guess: '
		guess = gets.chomp.lower
	end

end