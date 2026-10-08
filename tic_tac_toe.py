board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--#---#--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--#---#--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for a,b,c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
def board_full():
    return " " not in board

current_player = "X"
print("Tic-Tac-Toe!")
print("Wähle eine Position von 1 bis 9:")
while True:
    print_board()
    try:
        position = int(input(f"Spieler {current_player}, wähle eine Position: "))
    except ValueError:
        print("Bitte gib eine Zahl ein!")
        continue
    if position < 1 or position > 9:
        print("Bitte wähle eine Zahl zwischen 1 und 9!")
        continue
    position -= 1
    if board[position] != " ":
        print("Diese Position ist bereits belegt!")
    board[position] = current_player
    if check_winner(current_player):
        print_board()
        print(f"Spieler {current_player} hat gewonnen!")
        break
    if board_full():
        print_board()
        print("Unentschieden!")
        break
    print('test test')
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"