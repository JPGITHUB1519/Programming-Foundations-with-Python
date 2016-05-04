
def convert_letter(letter) :

	if letter == 'a' :

		return 0

	if letter == 'b' :

		return 1

	if letter == 'c' :

		return 2

	if letter == 'd' :

		return 3

	if letter == 'e' :

		return 4

	if letter == 'f' :

		return 5

	if letter == 'g' :

		return 6

	if letter == 'h' :

		return 7

def change_position(board,aw) :

	if len(aw) == 2 :
		pos = [convert_letter(aw[0]),int(aw[1])]
	else :
		


	split_board = board.split_board


	split_board[pos[0], pos[1]] = 
	


board = ["|WR|WN|WB|WQ|WK|WB|WN|WR| 1 ", 
		 "|WP|WP|WP|WP|WP|WP|WP|WP| 2",
		 "|__|__|__|__|__|__|__|__| 3",
		 "|__|__|__|__|__|__|__|__| 4",
		 "|__|__|__|__|__|__|__|__| 5",
		 "|__|__|__|__|__|__|__|__| 6",
		 "|BP|BP|BP|BP|BP|BP|BP|BP| 7",
		 "|BR|BM|BB|BQ|BK|BB|BN|BR| 8",
		 "  A  B  C  D  E  F  G  H\n"]

print change_position(board,"e5")




#1.e4 e5

for i in board :

	print i

input()
