from random import randint

#subprogramas
def printBoard(b):
    print(b[0]," |",b[1],"|",b[2],"\n",'----------',"\n",b[3],"|",b[4],"|",b[5],"\n",'----------',"\n",b[6],"|",b[7],"|",b[8])

def playerName(p):
    print("digite o nome do player",p,": ")
    return input()

def checkWin(b, s):
    return ((b[0] == s and b[1] == s and b[2] == s) or  # linha sup
            (b[3] == s and b[4] == s and b[5] == s) or  # linha meio
            (b[6] == s and b[7] == s and b[8] == s) or  # linha inf
            (b[0] == s and b[3] == s and b[6] == s) or  # coluna esq
            (b[1] == s and b[4] == s and b[7] == s) or  # coluna meio
            (b[2] == s and b[5] == s and b[8] == s) or  # coluna dir
            (b[0] == s and b[4] == s and b[8] == s) or  # diag principal
            (b[2] == s and b[4] == s and b[6] == s))    # diag aux

def getTurn():
    aux = True
    while aux:
        try:
            first = int(input("gostaria de ser o primeiro(1) ou segundo(2)?: "))
            if first == 1:
                m = '0'
                aux = False
                continue
            if first == 2:
                m = 'X'
                aux = False
                continue
            else:
                print("resposta invalida")

        except ValueError:
            print("somente numeros sao aceitos")

    return m

def checkDraw(b):
    return ' ' not in b

def getLevel(): #pergunta o level desejado
    aux = True
    while aux:
        try:
            l = int(input("qual nivel deseja jogar (1)easy, (2)medium, (3)hard : "))
            if l!= 1 and l!= 2 and l!= 3 :
                print("resposta invalida: ")
                l = getLevel()
            else:
                aux = False
        except ValueError:
            print("somente numeros sao aceitos")
    return l

def moveNpc(l,b,pm):
    if l == 1:
        m = getComputerMoveEasy(b)
    if l == 2:
        m = getComputerMoveMedium(b,pm)
    if l == 3:
        m = getComputerMoveHard(b,pm)
    return m

def getType():
    aux = True
    while aux:
        try:
            t = int(input("qual tipo de jogo deseja jogar\n humano X humano(1): \n humano X maquina(2): \n maquina X maquina(3): "))
            if t!= 1 and t!= 2 and t!= 3 :
                print("resposta invalida: ")
            else:
                aux = False
        except ValueError:
            print("somente numeros são aceitos")

    return t

def getBoardCopy(b):
    copyB = []
    for i in b:
        copyB.append(i)
    return copyB

def testWinMove(b, pm, i):
    copyB = getBoardCopy(b)
    copyB[i] = pm
    return checkWin(copyB,pm)

def getComputerMoveHard(b, pm):
    if pm == '0':
        markerAux = 'X'
    else:
        markerAux = '0'
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, pm, i):
            return i
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b,markerAux , i):
            return i
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    if b[4] == ' ':
        return 4
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i

def getComputerMoveMedium(b,pm):
    aux = True
    if pm == '0':
        markerAux = 'X'
    else:
        markerAux = '0'
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, pm, i):
            return i
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b,markerAux , i):
            return i
    while aux:
        m = randint(0,8)
        if b[m] == ' ':
            aux = False
    return m

def getComputerMoveEasy(b):
    while aux:
        m = randint(0,8)
        if b[m] == ' ':
            aux = False
    return m

#programa principal
Playing = True
while Playing:
    gameLevel = 0
    gameType = 0
    inGame = True
    board = [' '] * 9
    names = [' '] * 2
    repet = " "
    dificuldades = ["easy","medium","hard"]
    gameType=getType()
    if gameType == 1:
        for i in range(2):
            names[i] = playerName(i+1)
        printBoard(board)
        while inGame:
            print(names[0], "turn")
            playerMarker = '0'
            print("jogue uma casa de (1-9): ")
            move = int(input()) - 1
            if board[move] != ' ':
                print('Invalid move!')
                continue

            board[move] = playerMarker

            if checkWin(board, playerMarker):
                inGame = False
                printBoard(board)
                print(names[0],"ganhou")
                continue

            if checkDraw(board):
                inGame = False
                printBoard(board)
                print("foi um empate!!!")
                continue

            printBoard(board)
            print(names[1], "turn")
            playerMarker = "X"
            print("jogue uma casa de (1-9): ")
            move = int(input()) - 1
            if board[move] != ' ':
                print('movimento invalido')
                continue

            board[move] = playerMarker

            if checkWin(board, playerMarker):
                inGame = False
                printBoard(board)
                print(names[1],"ganhou")
                continue

            if checkDraw(board):
                inGame = False
                printBoard(board)
                print("foi um empate!!!")
                continue
            printBoard(board)

    if gameType == 2:
        gameLevel = getLevel()
        names[0] = playerName(1)
        playerMarker = (getTurn())
        printBoard(board)
        while inGame:
            if playerMarker == '0':
                print("jogue uma casa de (1-9): ")
                move = (int(input()) - 1)
                if board[move] != ' ':
                    print('Invalid move!')
                    continue
                board[move] = playerMarker
            else:
                print("maquina", dificuldades[gameLevel-1])
                move = moveNpc(gameLevel, board, playerMarker)
                board[move] = playerMarker
            printBoard(board)

            if checkWin(board, playerMarker):
                inGame = False
                printBoard(board)
                if playerMarker == '0':
                    print(names[0], "ganhou !")
                else:
                    print('maquina ganhou!')
                continue

            if checkDraw(board):
                inGame = False
                printBoard(board)
                print("foi um empate!!!")
                continue

            if playerMarker == '0':
                playerMarker = 'X'
            else:
                playerMarker = '0'

    if gameType == 3:
        playerMarker = '0'
        gameLevel = getLevel()
        while inGame:
            move = moveNpc(gameLevel, board, playerMarker)

            board[move] = playerMarker

            printBoard(board)

            if checkWin(board, playerMarker):
                inGame = False
                printBoard(board)
                if playerMarker == '0':
                    print("Bola ganhou!")
                else:
                    print("cruz ganhou!")
                continue

            if checkDraw(board):
                inGame = False
                printBoard(board)
                print("foi um empate!!!")
                continue

            if playerMarker == '0':
                playerMarker = 'X'
            else:
                playerMarker = '0'

    repet = (input("deseja jogar novamente digite (S)sim ou (N)nao: "))
    if repet == "s" or repet == "S":
        Playing = True
    else:
        Playing = False