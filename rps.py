player1 = input("Player 1, enter your choice (R/P/S): ")
player2 = input("Player 2, enter your choice (R/P/S): ")

if player1 == 'R' and player2 == 'S':
	print("Player 1 won!")
if player1 == 'S' and player2 == 'R':
	print("Player 2 won!")

if player1 == 'R' and player2 == 'P':
	print("Player 2 won!")
if player1 == 'P' and player2 == 'R':
	print("Player 1 won!")

if player1 == 'P' and player2 == 'S':
	print("Player 2 won!")
if player1 == 'S' and player2 == 'P':
	print("Player 1 won!")

if player1 == player2:
	print("It's a tie!")