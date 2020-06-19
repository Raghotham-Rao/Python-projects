def checkLine(board):
    # checking rows
    for i in range(3):
        c = 0
        if board[i][0] != '-':
            for j in range(3):
                if board[i][j] == board[i][0]:
                    c += 1
                    continue
            if c == 3:
                return board[i][0]

    # checking columns
    for i in range(3):
        c = 0
        if board[0][i] != '-':
            for j in range(3):
                if board[j][i] == board[0][i]:
                    c += 1
                    continue
            if c == 3:
                return board[0][i]

    # checking diagonals
    c = 0
    if board[0][0] != '-':
        for i in range(3):
            c += 1 if board[i][i] == board[0][0] else 0
        if c == 3:
            return board[0][0]

    c = 0
    if board[0][2] != '-':
        for i in range(3)[::-1]:
            c += 1 if board[2 - i][i] == board[0][0] else 0
        if c == 3:
            return board[0][2]

    return -1


def checkConsecutive(board):
    for i in range(3):
        if 'X' not in board[i] and board[i].count('O') == 2:
            return i, board[i].index('-')

    for i in range(3):
        c = [board[j][i] for j in range(3)]
        if 'X' not in c and c.count('O') == 2:
            return c.index('-'), i

    c = [board[0][0], board[1][1], board[2][2]]
    if 'X' not in c and c.count('O') == 2:
        return c.index('-'), c.index('-')

    c = [board[0][2], board[1][1], board[2][0]]
    if 'X' not in c and c.count('O') == 2:
        return c.index('-'), 2 - c.index('-')

    return -1


def minimax(board, depth, turn, vacancy):
    next_i = next_j =0

    if checkLine(board) == 'X':
        return 10

    if checkLine(board) == 'O':
        return -10

    if vacancy:
        if turn:
            curr_max = -1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '-':
                        board[i][j] = 'X'
                        val = minimax(board, depth + 1, not(turn), vacancy - 1)
                        try:
                            val = val[0]
                        except:
                            pass
                        if val > curr_max:
                            curr_max = val
                            next_i = i
                            next_j = j
                        board[i][j] = '-'
                        vacancy += 1
            return curr_max, next_i, next_j
        else:
            curr_min = 1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '-':
                        board[i][j] = 'O'
                        val = minimax(board, depth + 1, not(turn), vacancy - 1)
                        try:
                            val = val[0]
                        except:
                            pass
                        if val < curr_min:
                            curr_min = val
                            next_i = i
                            next_j = j
                        board[i][j] = '-'
                        vacancy += 1
            return curr_min, next_i, next_j
    else:
        return 0

# board = [
#     ['X', 'O', 'X'],
#     ['-', 'O', '-'],
#     ['O', '-', '-']
# ]
# ch = checkConsecutive(board)
# print(minimax(board, 0, True, 4) if ch == -1 else ch)