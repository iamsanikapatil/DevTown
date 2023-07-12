# ConstBoard Function

def ConstBoard(board):
	print("Curren State of the Board : \n\n ");

	for i in range(0,9):
		if ((i > 0 ) and (i % 3 == 0 )):
			print("\n");
		if (board[i] == 0):
			print("_", end = " ");
		if (board[i] == -1 ):
			print("X", end = " ");
		if (board[i] == 1):
			print("O", end = " ");
	print("\n \n ");


# get user1 Input 

def User1Turn(board):
	pos = int(input("Enter X's position from [1,2,3,4,...9]"));

	if (board[pos-1] != 0):				#empty state
		print("Wrong Move ....!");
		exit(0);   						#stop the game 

	board[pos-1] =-1 ;

# get user2 Input 

def User2Turn(board):
	pos = int(input("Enter O's position from [1,2,3,4,...9]"));

	if (board[pos-1] != 0):				#empty state
		print("Wrong Move ....!");
		exit(0);   						#stop the game 

	board[pos-1] =1 ;

# Analyze Function

def analyzeboard(board):

	cb =[ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6] ];

	for i in range(0,9):
		if (board[cb[i][0] != 0] and 
			board[cb[i][0]] == board[cb[i][1]] and 
			board[cb[i][0]] == board[cb[i][2]]):
			
			return board[cb[i][0]] ;
	return 0 ;

def minmax(board, player):
	x = analyzeboard(board);

	if (x!= 0):
		return (x*player)

	pos = -1 ;
	value = -2 ;
	for i in range(0,9):
		board[i] = player; 
		score = -minmax(board, player * -1);
		board[i] = 0 ;

		if (score>value):
			value = score ;
			pos = i ;
	if (pos == -1 ):
		return 0 ; 
	return value ; 

# computer Turn 

def CompTurn(board):
	pos = -1 ;
	value = -2 ;
	for i in range(0,9):
		board[i] = - 1 ;
		score = -minmax(board, -1);
		board[i] = 0 ;

		if (score>value):
			value = score ;
			pos = i ;
	board[pos] = 1 ;

# start here ------- >>>>>>>>

def main():

	# it is a string  and I want to convert into int 

	choice = int(input("Enter 1 for Single, 2 for Multiplayer :  "));

	# list is data-structure in python , Container , like bucket, ,
	# List useful data-structure === list 

	# numerical representation of GAME-BOARD - Empty State 

	board = [0,0,0 , 0,0,0, 0,0,0 , 0,0,0]

	if (choice ==1 ):
		print("Computer: 0 VS You: X ");
		player = int(input("Enter to play 1(st) or 2(nd) : "));

		for i in range(0,9):
			if (analyzeboard(board)!= 0):
				break ; 
			if ((i + player) % 2 == 0 ):
				CompTurn(board);
			else :
				ConstBoard(board); # human can see the board
				User1Turn(board);	# input from user1

	else:
		for i in range(0,9):
			if (analyzeboard(board) != 0 ):
				break ; 
			if ((i % 2 == 0 )):
				ConstBoard(board);
				User1Turn(board);
			else :
				ConstBoard(board); # human can see the board
				User2Turn(board);	# input from user2 

	# final check 

	x = analyzeboard(board);

	if(x==0):
		ConstBoard(board);
		print("Draw...!");
	if(x== -1 ):
		
		ConstBoard(board);
		print("PLayer X Wins ! ! ! ooo Looses");
	if(x== + 1):
		ConstBoard(board);
		print("PLayer O Wins ! ! ! ooo Looses");



main();




	