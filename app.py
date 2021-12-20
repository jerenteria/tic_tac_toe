# stores the board
board = [' ', for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[6] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le) or

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \`X\' (1-9): ')
        try:
            move = int(move)
            # make sure the user input is within range
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a random within the range!')
        except:
            print('Please type a number!')


def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    if(board.count(' ') > 1):
        return True
    else:
        return False

def main():
    print("Welcome to Tic Tac Toe!")
    printBoard()

    while not(isBoardFull(board)):
        # if Os is the winner then no need for a player move
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("Sorry, O\'s won this game!")
            break

        # if Xs is the winner then no need for a player move
        if not(isWinner(board, 'O')):
            compMove()
            printBoard()
        else:
            print("X\'s won this game! Good Job!")
            break


    # if board is full then game is tied and is not over
    if isBoardFull(board):
        print("Tie Game!")