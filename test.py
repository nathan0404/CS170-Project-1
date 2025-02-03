board = [[1, 2, 3,], 
         [4, 5, 0]]
row = 1
col = 2
directions = [[1, 0],
                      [-1, 0],
                      [0, 1],
                      [0, -1]]

for dr, dc in directions:
    print(dr+row, dc+col)

temp = board.copy()
print(board)
temp[0][0] = 100
print(temp)