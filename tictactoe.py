import random

def drawBoard(board):
    print ''
    print '   |   |'
    print ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2]
    print '   |   |'

def selectPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print '\nDo you want to be X or O?',
        letter = raw_input().upper()
    return letter

def determineOrder():
    if random.randint(0,1) == 0:
        return 'player'
    else:
        return 'ai'

def playAgain():
    rematch = ''
    while not (rematch == 'yes' or rematch == 'no'):
        print '\nDo you want to play again (yes or no)?',
        rematch = raw_input().lower()
    return rematch.startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[6] == letter and board[7] == letter and board[8] == letter) or
    (board[3] == letter and board[4] == letter and board[5] == letter) or
    (board[0] == letter and board[1] == letter and board[2] == letter) or
    (board[6] == letter and board[3] == letter and board[0] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[6] == letter and board[4] == letter and board[2] == letter) or
    (board[8] == letter and board[4] == letter and board[0] == letter))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '0 1 2 3 4 5 6 7 8'.split() or not isSpaceFree(board, int(move)):
        print '\nWhat is your next move (0-8)?',
        move = raw_input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board):
    # choose a completely random square
    return chooseRandomMoveFromList(board, [0, 1, 2, 3, 4, 5, 6, 7, 8])

def isBoardFull(board):
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True

def main():
    print('Welcome to Tic Tac Toe!')

    while True:
        theBoard = [' '] * 10
        playerLetter = selectPlayerLetter()
        computerLetter = 'O' if playerLetter == 'X' else 'X'
        turn = determineOrder()
        print('\nThe ' + turn + ' will go first.')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('\nHooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('\nThe game is a tie!')
                        break
                    else:
                        turn = 'ai'
            else:
                move = getComputerMove(theBoard)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('\nThe computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('\nThe game is a tie!')
                        break
                    else:
                        turn = 'player'
        if not playAgain():
            break

if __name__=='__main__':
	main()
