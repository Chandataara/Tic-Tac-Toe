board = [
	[' ', 1, 2, 3, ''],
	['a', 'E', 'E', 'E', ''],
	['b', 'E', 'E', 'E', ''],
	['c','E', 'E', 'E', '']
]



def print_board(bo):
	for i in range(len(bo)):
		if not i % 1 and i != 0:
			print('\n\n')
			
		for j in range(len(bo[0])):
			if not j % 1 and j != 0:
				print(5 * ' ', end="")
	
			if j == 5:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ", end="")

player1 = input('Player1\'s name: ')
player2 = input('\nPlayer2\'s name: ')
print(f'\nTo play a square write the letter on the left and then the number on top. For example... to play the middle square you have to write the letter on the left most side then the number on the top like the middle square will be b2 like below:')
player_chooser = 0
print_board(board)
possible_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
cant_be_played = set([])
while 1:
	row1, row2, row3, row4 = board
	a1, a2, a3 = row2[1 : 4]
	b1, b2, b3 = row3[1 : 4]
	c1, c2, c3 = row4[1 : 4]
	if not player_chooser % 2:
		move = input(f'\n{player1}, please play your move: ')
		if not move in cant_be_played and move in possible_moves:
			cant_be_played.add(move)
			possible_moves.pop(possible_moves.index(move))
			if move == 'a1':
				a1 = 'O'
			elif move == 'a2':
				a2 = 'O'
			elif move == 'a3':
				a3 = 'O'
			elif move == 'b1':
				b1 = 'O'
			elif move == 'b2':
				b2 = 'O'
			elif move == 'b3':
				b3 = 'O'
			elif move == 'c1':
				c1 = 'O'
			elif move == 'c2':
				c2 = 'O'
			elif move == 'c3':
				c3 = 'O'

			cant_be_played.add(move)
		else:
			continue
	
	else:
		move = input(f'\n{player2}, please play your move: ')
		if not move in cant_be_played and move in possible_moves:
			cant_be_played.add(move)
			possible_moves.pop(possible_moves.index(move))
			if move == 'a1':
				a1 = 'X'
			elif move == 'a2':
				a2 = 'X'
			elif move == 'a3':
				a3 = 'X'
			elif move == 'b1':
				b1 = 'X'
			elif move == 'b2':
				b2 = 'X'
			elif move == 'b3':
				b3 = 'X'
			elif move == 'c1':
				c1 = 'X'
			elif move == 'c2':
				c2 = 'X'
			elif move == 'c3':
				c3 = 'X'

			cant_be_played.add(move)			
		else:
			continue

	board = [
	[' ', 1, 2, 3, ''],
	['a', a1, a2, a3, ''],
	['b', b1, b2, b3, ''],
	['c', c1, c2, c3, '']
	]
	print_board(board)
	player_chooser += 1
	
	
	def win():
		three_in_rows = [
		[a1, a2, a3],
		[b1, b2, b3],
		[c1, c2, c3],
		[a1, b1, c1],
		[a2, b2, c2],
		[a3, b3, c3],
		[a1, b2, c3],
		[a3, b2, c1]
	]
	
		for x in three_in_rows:
			if x == ['O', 'O', 'O']:
				print(f'{player1} wins!')
				return 'win'
				break
			elif x == ['X', 'X', 'X']:
				print(f'{player2} wins!')
				return 'win'
				break
			elif len(possible_moves) == 1 \
				and len(cant_be_played) == 8:
				print('You tied!')
				return 'tied'
				
	result = win()
	if result == 'win':
		break
	elif result == 'tied':
		break
