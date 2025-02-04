
goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
#board = [[1, 2, 3], [4, 5, 0], [7, 8, 6]] #test baord 
board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] #test baord 
directions = [[1, 0],
                      [-1, 0],
                      [0, 1],
                      [0, -1]]


def gScore(board):
    goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
    score = 0
    row = 0
    col = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == goalBoard[row][col]:
                print("score:", score, row, r, col, c)
                score += abs((row-r) + (col-c))
                if col >= 2:
                    col = 0
                    row += 1
                else:
                    col += 1
                print("incremetn row and col", row, col)
                print()
    print("final score", score)
    return


gScore(board)