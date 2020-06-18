winList = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


# Displays current board
def display(board):
    board_display = [f' {board[0]} | {board[1]} | {board[2]} \n',
                     f' {board[3]} | {board[4]} | {board[5]} \n',
                     f' {board[6]} | {board[7]} | {board[8]} \n']
    for i in board_display:
        print(i)


# Check if someone has won after every turn
def win_check(current_player, board):
    if current_player == '1':
        player = 'X'
    else:
        player = 'O'

    player_indexes = []

    for index, value in enumerate(board):
        if value == player:
            player_indexes.append(index)
    player_indexes = tuple(player_indexes)

    for i in winList:
        if set(player_indexes).issuperset(i):
            return True
    return False


def switch_players(current_player):
    if current_player == '1':
        return '2'
    else:
        return '1'


def main():
    current_player = '1'

    turn_count = 0

    board = ['_'] * 9

    display(board)

    while True:
        try:
            player_move = int(input(f"Player {current_player}, please choose a position from 0 - 8 that is not taken: "))
            if player_move < 0:
                print("You must enter a number between 0 and 8, try again.")
                continue
            while not board[player_move] == '_':
                player_move = int(input("Space taken, please choose another position from 0 - 8: "))
        except ValueError:
            print("You did not enter a digit, try again.")
            continue
        except IndexError:
            print("You must enter a number between 0 and 8, try again.")
            continue

        if current_player == '1':
            board[player_move] = 'X'
        else:
            board[player_move] = 'O'

        turn_count += 1

        display(board)

        if turn_count > 4:
            if win_check(current_player, board):
                break

        current_player = switch_players(current_player)

    if current_player == '1':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == '__main__': main()
