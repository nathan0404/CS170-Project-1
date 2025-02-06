
goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
#board = [[1, 2, 3], [4, 5, 0], [7, 8, 6]] #test baord 
board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] #test baord 012345678
#board = [[1, 2, 3], [0, 4, 5], [7, 8, 6]] #3 depth  123045786
directions = [[1, 0],
                      [-1, 0],
                      [0, 1],
                      [0, -1]]


def gScore(board):
    curNum = 1
    goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
    score = 0
    row = 0
    col = 0
    while curNum <= 8:
        for r in range(3):
            for c in range(3):
                if board[r][c] == curNum:
                    print("looking for:", curNum)
                    tempCol = abs(col-c)
                    tempRow = abs(row-r)
                    score += tempCol + tempRow
                    if col >= 2:
                        col = 0
                        row += 1
                    else:
                        col += 1
                    print("found calculating distance:", tempCol+tempRow)
                    curNum += 1
                    print("cur score", score)
                    print()
    print()
    print("final score", score)
    return


gScore(board)