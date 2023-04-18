def rowFull():
    # check if any row is full, with same symbol
    symbol = 'x'
    for row in board:
        if row.count(symbol) == 3:
            return True

    symbol = 'o'
    for row in board:
        if row.count(symbol) == 3:
            return True

    return False


def colFull():
    symbol = 'x'
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True

    symbol = 'o'
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True

    return False


def diagFull():
    symbol = 'x'
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    symbol = 'o'
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

def boardFull():
    emptyCount = 0
    for row in board:
        emptyCount += row.count('-')
        
    if emptyCount == 0:
        return True
    else:
        return True


board = [['-' for _ in range(3)] for _ in range(3)]
print(*board,sep="\n")
while not rowFull() and not colFull() and not diagFull() and not boardFull():
    move1 = [int(x) for x in input("Player1: Enter row and col: ").split()]
    move2 = [int(x) for x in input("Player2: Enter row and col: ").split()]

    if board[move1[0]][move1[1]] != '-' or board[move2[0]][move2[1]] != '-':
        print("Invalid move")
        continue

    board[move1[0]][move1[1]] = "x"
    board[move2[0]][move2[1]] = "o"
    print(*board,sep="\n")
print("Game Over")
