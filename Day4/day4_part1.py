# day4_part1.py

def function():
	return 1

def parse_input_file(file):
	draws = []
	boards = []
	file_ln = 0
	board_ln = 0
	current_board = ''
	f = open(file, "r")
	for line in f:
		file_ln += 1
		line = line.strip()
		if (file_ln == 1):
			# This is the list of numbers drawn in order
			draws = line.split(',')
		else:
			# Blank lines are delimiters
			if (line == ''):
				# Starting a new board
				current_board = ''
				board_ln = 0
			else:
				# Otherwise, we're reading part of a board
				board_ln += 1
				current_board = current_board + line + ' '
				if (board_ln == 5):
					boards.append(current_board.split())
	f.close()
	return(draws, boards)


def check_for_winner(drawn, boards):
	we_have_a_winner = False
	w = None # index of winner
	for b, board in enumerate(boards):
		lines = [
			board[0:5], board[5:10], board[10:15], board[15:20], board[20:25],
			board[0::5], board[1::5], board[2::5], board[3::5], board[4::5]
		]
		for l, line in enumerate(lines):
			# "List Comprehensions"
			if not [x for x in line if x not in drawn]:
				we_have_a_winner = True
				w = b
	return (we_have_a_winner, w)

def main(file):
	# Setup
	(draw_order, boards) = parse_input_file(file)
	we_have_a_winner = False
	i = 4 # impossible to win until the 5th number is drawn, so start here
	drawn = []

	# Play
	while not we_have_a_winner:
		i += 1
		drawn = draw_order[0:i] # remember, ith element is not included
		(we_have_a_winner, winning_board_index) = check_for_winner(drawn, boards)
	
	# Calculate results
	winning_board = boards[winning_board_index]
	winning_number = draw_order[i - 1] # because the ith element was not included
	remaining_numbers = [int(x) for x in winning_board if x not in drawn]
	score = int(winning_number) * sum(remaining_numbers)

	print("Draw order: ", draw_order)
	print("Winning board: ", winning_board)
	print("Winning Board Index: ", winning_board_index)
	print("Winning number: ", winning_number)
	print("Winning drawn index: ", i)
	print("Score is: ", score)



	print("Done!")


main('input.txt')
