# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name: Fazell Dost
# Student Number: 48838830
# ----------------

# Write your classes and functions here

def num_hours() -> float:
    """
    Returns the number of hours spent on the project.
    
    Returns: 
    The number of hours spent, being 6.9.
    >>>num_hours()
    6.9
    
    """
    return 6.9

def generate_initial_board() -> list[str]:
    """
    Returns a list with each of the board's columns as 8 invividual strings.
    
    Returns: 
    A blank board.

    >>>generate_initial_board()
    ['--------', '--------', '--------', '--------', '--------', '--------', 
    '--------', '--------']
    """
    board = []
    for i in range(BOARD_SIZE):
        board.append(BLANK_PIECE*BOARD_SIZE)
    return board

def is_column_full(column: str) -> bool:
    """
    Returns whether or not the column the player is attempting to add a piece 
    to is full by checking if the top piece of the desired column is not blank.
    
    Arguments: 
    A column of the board.
    Returns: 
    True if the column is full, False if the column is not.
    Preconditions: 
    The column will represent a valid column state(i.e. no blank 
    spaces between pieces.)
    
    >>>is_column_full('---XOXOX')
    False
    >>>is_column_full('OXOXOXOX')
    True
    """
    if column[0] == BLANK_PIECE:
        return False
    else:
        return True

def is_column_empty(column: str) -> bool:
    """
    Returns whether or not the column the player is attempting to remove a 
    piece from is empty by checking if the bottom piece of the deisred column 
    is blank.

    Arguments: 
    A column of the board.
    Returns: 
    True if the column is empty, False if the column is not.
    Preconditions: 
    The column will represent a valid column state(i.e. no blank 
    spaces between pieces.)
    
    >>>is_column_empty('----OXOX')
    False
    >>>is_column_empty('--------')
    True
    """
    if column[BOARD_SIZE-1] == BLANK_PIECE: #indexing starts at 0.
        return True
    else:
        return False

def display_board(board: list[str]) -> None:
    """
    Displays the current state of the game's board from the inputted list.
    
    Arguments: 
    The entire game board.
    Returns: 
    The game board in an aesthetically pleasing format that is easier 
    to play with.
    Precondition: 
    The input board should contain exactly 8 strings with 8 
    characters each.

    >>>board = ['--------', '----OOOO', 'XXXXXXXX', '--------', '------XO',
    '--------', '---XXOXO', '--------']
    >>>display_board(board)
    |-|-|X|-|-|-|-|-|
    |-|-|X|-|-|-|-|-|
    |-|-|X|-|-|-|-|-|
    |-|-|X|-|-|-|X|-|
    |-|O|X|-|-|-|X|-|
    |-|O|X|-|-|-|O|-|
    |-|O|X|-|X|-|X|-|
    |-|O|X|-|O|-|O|-|
     1 2 3 4 5 6 7 8 
    """
    
    for row in range(BOARD_SIZE):
        dboard = COLUMN_SEPARATOR
        for column in range(BOARD_SIZE):
            dboard += board[column][row]
            dboard += COLUMN_SEPARATOR
        print(dboard)
    print(" 1 2 3 4 5 6 7 8 ")

def check_input(command: str) -> bool:
    """
    Checks if the command entered by the player is a valid command, displaying 
    the relevant error message otherwise.

    Arguments: 
    The user's inputted command.
    Returns: 
    Returns True is the command is formatted correctly, False otherwise 
    along with the relevant error message.
    Preconditions: The user entered column must be a single digit number.

    >>>check_input("a1")
    True
    >>>check input("a9")
    Invalid column, please enter a number between 1 and 8 inclusive
    False
    >>>check_input("1r")
    Invalid command. Enter 'h' for valid command format
    False
    """
    if command:
        if command in ['q', 'Q', 'h', 'H']:
            return True
        elif command[0] in ['a', 'A', 'r', 'R']:
            if len(command) == 2 and command[1].isdigit():
                if 0 < int(command[1]) < 9:
                    return True
                else:
                    print(INVALID_COLUMN_MESSAGE)
                    return False
            elif len(command) != 2:
                print(INVALID_FORMAT_MESSAGE)
                return False
            else:
                return True
        else:
            print(INVALID_FORMAT_MESSAGE)
            return False
    else:
        print(INVALID_FORMAT_MESSAGE)
        return False

def get_action() -> str:
    """
    Checks the player's input, returning said input if it is valid.

    Returns: 
    The command if the input is valid, None otherwise.
    Preconditons: 
    check_input() returns a bool.

    >>>get_action()
    Please enter action (h to see valid commands): g
    Invalid command. Enter 'h' for valid command format
    >>>get_action()
    Please enter action (h to see valid commands): r4
    'r4'
    """
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        if check_input(command):
            return command

def add_piece(board: list[str], piece: str, column_index: int) -> bool:
    """
    Adds a piece to the desired column, piece will be on top of already 
    existing pieces.

    Arguments: 
    The board, the piece and the desired column's index.
    Returns: 
    Adds the piece to the board and returns True if the column is not 
    full, does not add the piece and returns False otherwise.
    Precondition: 
    The board will have exactly 8 strings each with 8 strings 
    each, and represent a valid game state. The specified column index is 0 to 
    7 inclusive. The given piece will be exactly 1 character in length.

    >>> board = ['--------', '----OOOO', 'XXXXXXXX', '--------', '------XO',
    '--------', '---XXOXO', '--------']
    >>> add_piece(board, "X", 1)
    True

    >>> board = ['--------', '---XOOOO', 'XXXXXXXX', '--------', '------XO', 
    '--------', '---XXOXO', '--------']
    >>> add_piece(board, "O", 2)
    You can't add a piece to a full column!
    False
    """
    if not is_column_full(board[column_index]):
        temp_column = ""
        for row in range(BOARD_SIZE-1, -1, -1):
            if board[column_index][row] == BLANK_PIECE:
                temp_column += piece
                temp_column += BLANK_PIECE*(BOARD_SIZE-len(temp_column))
                board[column_index] = temp_column[::-1]
                return True

            else:
                temp_column += (board[column_index][row])
    else:
        print(FULL_COLUMN_MESSAGE)
        return False
            
    
def remove_piece(board: list[str], column_index: int) -> bool:
    """
    Removes a piece from the bottom the desired column, leading to the pieces 
    on top of it to fall down.

    Argmuents: 
    The board and the desired column's index.
    Returns: 
    Removes the piece from the bottom of the board and returns True if 
    the column is not empty, does not add the piece and returns 
    False otherwise.
    Precondition: 
    The board will have exactly 8 strings each with 8 strings 
    each, and represent a valid game state. The specified column index is 0 to 
    7 inclusive. The given piece will be exactly 1 character in length.

    >>> board = ['--------', '----OOOO', 'XXOOOXXX', '--------', '------XO',
    '--------', '---XXOXO', '--------']
    >>> remove_piece(board, 2)
    True

    >>> board = ['--------', '----OOOO', '-XXOOOXX', '--------', '------XO', 
    '--------', '---XXOXO', '--------']
    >>> remove_piece(board, 0)
    You can't remove a piece from an empty column!
    False
    """
    if is_column_empty(board[column_index]):
        print(EMPTY_COLUMN_MESSAGE)
        return False
    else:
        temp_column = ""
        for row in range(BOARD_SIZE-1, 0, -1):
            temp_column += board[column_index][row-1]
        temp_column += BLANK_PIECE
        board[column_index] = temp_column[::-1]
        return True
        
def determine_winner(winner: list[int], piece_check: str) -> None:
    """
    Checks if the inputted string, being the four pieces in a row, and 
    determines which, if any player should win by adding player's number 
    to the 'winner' list.

    Arguments: 
    The list of winners for the turn, the four pieces in a row
    Preconditions: 
    Piece check only has one of the three valid piece states.
    """

    if piece_check.count(PLAYER_1_PIECE) == REQUIRED_WIN_LENGTH:
        winner.append(1)
    if piece_check.count(PLAYER_2_PIECE) == REQUIRED_WIN_LENGTH:
        winner.append(2)

def check_win(board: list[str]) -> Optional[str]:
    """
    Checks every possible victory on the board, then determines if either 
    player has won, if there is a draw or if no one has won yet. A victory is 
    when there is 4 of the same piece in a straight line.

    Arguments: 
    The board.
    Returns: 
    The player's piece if one player wins, and the blank piece if 
    there is a draw. Returns None if no one wins.
    Preconditions: 
    The specified board will contain exactly 8 strings with 
    exactly 8 characters each. Every character will be 'X', 'O', or '-'.

    >>>board = ['------XO', '-------O', '--------', '--------', '-------O',
    '--------', '--------', '------XX']
    >>> check_win(board)

    >>> board = ['-------O', '------OX', '-----OXO', '---XOOXX', '--------',
    '--------', '--------', '--------']
    >>> check_win(board)
    'O'

    >>> board = ['-------X', '-------X', '------OX', '---OOOXX', '--------',
    '--------', '--------', '--------']
    >>> check_win(board)
    'X'

    >>> board = ['---XXXXO', '-------O', '-------O', '-------O', '--------',
    '--------', '--------', '--------']
    >>> check_win(board)
    '-'
    """
    winner = []
    #check horizontal wins
    for column in range(BOARD_SIZE-(REQUIRED_WIN_LENGTH-1)):
        for row in range(BOARD_SIZE):
            piece_check = ''
            for offset in range(REQUIRED_WIN_LENGTH):
                #offset determines the piece in a line of 4 being checked
                piece_check += board[column+offset][row]
            determine_winner(winner, piece_check)

    #check vertical wins
    for column in range(BOARD_SIZE):
        for row in range(BOARD_SIZE-(REQUIRED_WIN_LENGTH-1)):
            determine_winner(winner, board[column][row:row+REQUIRED_WIN_LENGTH])

    #check diagonal (down-right) wins
    for column in range(BOARD_SIZE-(REQUIRED_WIN_LENGTH-1)):
        for row in range(REQUIRED_WIN_LENGTH, BOARD_SIZE, 1):
            piece_check = ''
            for offset in range((REQUIRED_WIN_LENGTH)):
                #offset determines the piece in a line of 4 being checked
                piece_check += board[column+offset][row-offset]
            determine_winner(winner, piece_check)

    #check diagonal (up-right) wins
    for column in range(BOARD_SIZE-(REQUIRED_WIN_LENGTH-1)):
        for row in range(BOARD_SIZE-(REQUIRED_WIN_LENGTH-1)):
            piece_check = ''
            for offset in range((REQUIRED_WIN_LENGTH)): 
                #offset determines the piece in a line of 4 being checked
                piece_check += board[column+offset][row+offset]
            determine_winner(winner, piece_check)

    #return winning player
    if 1 in winner and 2 in winner:
        return BLANK_PIECE
    if 1 in winner:
        return PLAYER_1_PIECE
    if 2 in winner:
        return PLAYER_2_PIECE

def play_game() -> None:
    """
    The game state. Plays the game using all of the previous functions until 
    either player wins, a draw occurs, or either player quits.
    """
    turn = 0
    PIECES = [PLAYER_1_PIECE, PLAYER_2_PIECE]
    board = generate_initial_board()
    is_success = True
    while True:
        if is_success or com in ['h', 'H']:
            display_board(board)
            if check_win(board):
                if check_win(board) == PLAYER_1_PIECE:
                    print(PLAYER_1_VICTORY_MESSAGE)
                elif check_win(board) == PLAYER_2_PIECE:
                    print(PLAYER_2_VICTORY_MESSAGE)
                elif check_win(board) == BLANK_PIECE:
                    print(DRAW_MESSAGE)
                break
            #even turns are player 1, odd turns are player 2, turns start at 0
            if (turn%2) == 0:
                print(PLAYER_1_MOVE_MESSAGE)
            if (turn%2) == 1:
                print(PLAYER_2_MOVE_MESSAGE)
        com = get_action()
        if com in ['q', 'Q']:
            return
        elif len(com) > 1 and (com[0] in ['a', 'A']): #aX command
            is_success = add_piece(board, PIECES[turn%2], int(com[1])-1)
        elif len(com) > 1 and (com[0] in ['r', 'R']): #rX command
            is_success = remove_piece(board, int(com[1])-1)
        elif com in ['h', 'H']: #H command
            print(HELP_MESSAGE)
            is_success = False
        if is_success:
            turn += 1

def main() -> None:
    """
    The main function, runs the game loop and asks the user if they want to 
    play again after leaving the game state.
    """
    is_again = True
    while is_again:
        play_game()
        while True:
            again = input(CONTINUE_MESSAGE)
            if again in ['y', 'Y']:
                is_again =  True
                break
            else:
                is_again =  False
                break

if __name__ == "__main__":
    main()
