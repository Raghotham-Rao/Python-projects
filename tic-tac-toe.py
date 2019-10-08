from minimax import checkLine, minimax, checkConsecutive


def printBoard(board):
    for i in board:
        print(*i)
    print()


def computer(board, o_s, turn_no):
    if turn_no == 1:
        if o_s[-1] in [(0, 0), (2, 2), (2, 0), (0, 2)]:
            board[1][1] = 'X'
        else:
            i, j = minimax(board, 0, True, 8)[1:]
            board[i][j] = 'X'
    elif turn_no == 3:
        s1 = ''.join(board[i][i] for i in range(3))
        s2 = ''.join(board[i][2 - i] for i in range(3))
        if any(i == 'OXO' for i in [s1, s2]):
            board[2][1] = 'X'
        else:
            ch = checkConsecutive(board)
            if ch != -1:
                i, j = ch
            else:
                i, j = minimax(board, 0, True, 9 - turn_no - 1)[1:]
            board[i][j] = 'X'
            return board
    else:
        try:
            ch = checkConsecutive(board)
            if ch != -1:
                i, j = ch
            else:
                i, j = minimax(board, 0, True, 9 - turn_no - 1)[1:]
            board[i][j] = 'X'
            return board
        except:
            print('Its a Draw')
    return board


ch = input('Hey there! Care for a game of tic tac toe?(y/n)\n')
while ch == 'y':
    print('- - -\n'*3)
    print('You: O\tComputer: X')
    print('\nEnter the position in the following format:\nrow_number<space>col_number')
    turn = 0
    board = [['-', '-', '-'] for i in range(3)]
    count = 0
    ur = uc = 0
    o_s = []
    while True:
        if turn == 9:
            print("It's a Draw")
            break
        if turn % 2 == 0:
            print('Your turn:')
            ur, uc = map(int, input().split())
            board[ur - 1][uc - 1] = 'O'
            o_s.append((ur - 1, uc - 1))
            count += 1
        else:
            print('Computer:')
            board = computer(board, o_s, turn)
        printBoard(board)
        check = checkLine(board)
        if check == 'O':
            print('You Won')
            break
        elif check == 'X':
            print('I Won')
            break
        turn += 1
        #break
    ch = input('Another Game?')