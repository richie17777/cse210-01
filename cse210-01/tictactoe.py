
'''
    Tictactoe: Ricahrd Darko Asare

    Here are the list of functions that will run the code
    - a function for the board 
    - a fuction to display the board 
    - a function to create the board
    - a function to check for a winner 
    - a function to check for a tie
    - a function to to switch between players
'''


def main():
    # call the switch_players function to 
    # switch between players deppendin on whhos turn it is
    player = switch_players("")

    # call the create_board function to show the grid from 0-9 
    board = create_board()

    # crite a while loop that calls the winner and draw funtion to 
    # keep looping until there is a winner or the tie.
    while not (winner(board) or draw(board)):
        display_board(board)
        handle_turns(player, board)
        player = switch_players(player)
    display_board(board)

    # display a message at the end of the game
    print("Good game. Thanks for playing!")

# write a function that creates 
# the square board of the game
def create_board():
    # Create a list to hold places on the board
    board = []
    # Write a loop that generates the place holders
    # and append to the end of the list
    for square in range(9):
        board.append(square + 1)
    return board

# write a fuction to display the board
def display_board(board):
    # Print a square gride of the board to 
    # display the screen in rows and columns
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# create a function determines if there was no winner.
# returns true if none of the players was able to select 
# three columns and rows completely.
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

# Create a function to check if ther's a winner
# the fuctions determins a winner when 
# a players selects three spots on a column or row.
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# Create a function to handle the turns of the players
# Create a promt message for the user/player to select a sllot
# Enable ther players name to occupy the selected slot
def handle_turns(player, board):
    square = int(input(f"{player} Choose a slot from (1-9): "))
    board[square - 1] = player

# Create a fuction to switch between players
# to decide who's turn it is to make a move and 
# switch places with the return value
def switch_players(user):
    if user == "" or user == "o":
        return "x"
    elif user == "x":
        return "o"

# Call main to start this program.
if __name__ == "__main__":
    main()