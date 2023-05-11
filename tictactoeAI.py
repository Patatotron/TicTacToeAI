import os
board = ["#","#","#","#","#","#","#","#","#"]

def WinnerX():
    if board[0] == board[1] == board[2] == 'x':
        return True
    elif board[3] == board[4] == board[5] == 'x':
        return True
    elif board[6] == board[7] == board[8] == 'x':
        return True
    elif board[0] == board[3] == board[6] == 'x':
        return True
    elif board[1] == board[4] == board[7] == 'x':
        return True
    elif board[2] == board[5] == board[8] == 'x':
        return True
    if board[0] == board[4] == board[8] == 'x':
        return True
    if board[2] == board[4] == board[6] == 'x':
        return True
def WinnerAI():
    if board[0] == board[1] == board[2] == 'o':
        return True
    elif board[3] == board[4] == board[5] == 'o':
        return True
    elif board[6] == board[7] == board[8] == 'o':
        return True
    elif board[0] == board[3] == board[6] == 'o':
        return True
    elif board[1] == board[4] == board[7] == 'o':
        return True
    elif board[2] == board[5] == board[8] == 'o':
        return True
    if board[0] == board[4] == board[8] == 'o':
        return True
    if board[2] == board[4] == board[6] == 'o':
        return True

def printboard():
    os.system('clear')
    for x in range(len(board)):
        print(board[x],end=' ')
        if (x + 1) % 3 == 0:
            print()
    print()

def PlaceAI():
    for move in range(0,9):
            if board[move] == '#':
                board[move] = 'o'
                if WinnerAI() == True:
                    board[move] = 'o'
                    return
                else:
                    board[move] = '#'
                    continue
            else:
                continue
    for move in range(0,9):
        if board[move] == '#':
            board[move] = 'x'
            if WinnerX() == True:
                board[move] = 'o'
                return
            else:
                board[move] = '#'
                continue
        else:
            continue

    for move in range(0,9):
            if board[4] == '#':
                board[4] = 'o'
                break
            if board[move] == '#':
                board[move] = 'o'
                return
def PlaceSign():
    while True:
        printboard()
        sign = int(input("Enter the location of where you want to place your sign: ")) - 1
        if board[sign] == '#':
            board[sign] = 'x'
            break
        else:
            continue

while True:
    if '#' not in board:
        os.system('clear')
        printboard()
        print("draw")
        break
    PlaceSign()
    if WinnerX():
        printboard()
        print("X won!")
        break
    PlaceAI()
    if WinnerAI():
        printboard()
        print("AI won!")
        break