
#board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780

#board = [[1, 2, 3], [4, 5, 0], [7, 8, 6]] #test baord 
#board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] #test baord 012345678
#board = [[1, 2, 3], [0, 4, 5], [7, 8, 6]] #3 depth  123045786
directions = [[1, 0],
                      [-1, 0],
                      [0, 1],
                      [0, -1]]


def gScoreMisplacedTile(board):
    curNum = 1
    #goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
    score = 0
    for r in range(3):
        for c in range(3):
            print("looking for:", curNum)
            if board[r][c] != curNum and curNum != 9:
                print("found curNum:", curNum)
                score += 1
                print("cur score", score)
                print()
            curNum += 1
    print()
    print("final score", score)
    return 


gScoreMisplacedTile(board)