#------- Global variables -------

# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If game is still going
game_still_going = True

# Who won?or a tie
winner = None

current_player = "X"


def display_board():
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])



def play_game():
    
    # Display the initial board
    display_board()
    
    #loop through turns
    while game_still_going:
        
        handle_turn(current_player)
        
        #check if the game is over
        check_if_game_over()
        
        #Flip to the other player
        flip_player()
    
    #the game has ended
    if winner == "X" or winner == "O":
            print(winner + " won.")
    elif winner == None:
            print("Tie.")



#handle a single turn at an arbitrary player
def handle_turn(player):
    
    print("\n"+ player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid :
        
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input.Choose a position from 1-9:")
    
        position = int(position) - 1
    
        if board[position] == "-" :
            valid = True
        else:
            print("\n" + "You can't go there. TRY AGAIN ")
    
    
    board[position] = player
    
    display_board()
    


def check_if_game_over():
    check_for_winner()
    check_if_tie()



def check_for_winner():
    
    global winner
    
    #check rows
    row_winner = check_rows()
    
    #check columns
    column_winner = check_columns()
    
    #check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner 
   
    elif column_winner:
        winner = column_winner
    
    elif diagonal_winner:
        winner = diagonal_winner 
        
    else:
        winner = None
    


def check_rows():
    
    #set global variables
    global game_still_going
    
    #Check if any of the rows have the same value and are not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    #If any row does have a match,flag it as a win
    if row_1 or row_2 or row_3 :
        game_still_going = False
     
    # Return th winner
    if row_1 :
        return board[0]
    elif row_2  :
        return board[3]
    elif row_3 :
        return board[6]
    else:
        return None



def check_columns():
      
    #set global variables
    global game_still_going
    
    #Check if any of the columns have the same value and are not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    #If any column does have a match,flag it as a win
    if column_1 or column_2 or column_3 :
        game_still_going = False
     
    # Return th winner
    if column_1 :
        return board[0]
    elif column_2  :
        return board[1]
    elif column_3 :
        return board[2]
    else:
        return None
    



def check_diagonals():
    
    #set global variable
    global game_still_going 
    
    #check if any of the diagonals have the same value and are not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    
    #if the diagonals does have a match,flag that there is a win
    if diagonal_1 or diagonal_2 :
        game_still_going = False
        
    #Return the winner
    if diagonal_1 :
        return board[0]
    elif diagonal_2 :
        return board[2]
    else:
        return None



def check_if_tie():
    
    #set global variable
    global game_still_going 
    
    if "-" not in board :
        game_still_going = False
    
    
    return



def flip_player():
    
    #set global variable
    global current_player
    
    # to play game chance by chance
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
   


play_game()
