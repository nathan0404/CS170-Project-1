from collections import deque 
import copy

def main():    
    print("welcome to project 1: input 3 numbers for the first row.")
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 0, 8]]
    """
    for i in range(3):
        print("input 3 numbers seperated by space!")
        temp = input().split(" ")
        for j in range(3):
            temp[j] = int(temp[j])
        board.append(temp) """
    print()
    print("your baord is!", board)
    uniformCostSearch(board)


def uniformCostSearch(board):
    directions = [[1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]]
    depth = 0
    maxNodes = 0
    maxQueue = 0
    queue = deque()
    row, col = findZero(board)
    queue.append([board, row, col])

    while queue:
        maxQueue = max(maxNodes, len(queue))
        node, row, col = queue.popleft()
        maxNodes += 1
        if atGoalState(node):
            printResults(depth, maxNodes, maxQueue)
            return 
        for dc, dr in directions:
            tempRow = dr+row
            tempCol = dc+col
            if 0 <= tempRow <= 2 and 0 <= tempCol <= 2:
                boardCopy = copy.deepcopy(node)
                boardCopy[row][col] = node[tempRow][tempCol]
                boardCopy[tempRow][tempCol] = 0
                print()
                print("before", node)
                print("swtichable at", tempRow, tempCol)
                print("after", boardCopy)
                queue.append([boardCopy, tempRow, tempCol])
       
    


def findZero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                row = i
                col = j
    print("Zero is at!", row, col)
    return row, col
        
def atGoalState(board):
    goal_board = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    return True if board == goal_board else False
    
def printResults(depth, maxNodes, maxQueue):
    print("Soultion found!")
    print()
    print("Depth size of Tree:", depth)
    print("Max expaneded nodes: ", maxNodes)
    print("Max Queue size:", maxQueue)

main()