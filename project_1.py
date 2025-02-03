from collections import deque 
import copy

#these are testing boards that can be used
"""
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
    board = [[4, 1, 3], [0, 2, 6], [7, 5, 8]] #5 depth 
    board = [[5, 4, 2], [3, 0, 6], [7, 8, 1]] #18 depth 542306781

"""

def main():    
    print("welcome to project 1: input 3 numbers for the first row.")
    board = [[5, 4, 2], [3, 0, 6], [7, 8, 1]] #5 depth
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
    #directions are used later to simplifying the possible swaps the zero can make
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    depth, maxNodes, maxQueue = 0, 0, 0
    queue = deque()
    #row and col are used to keep location of the zero, reducing having to find the zero every new integration
    row, col = findZero(board)
    #appending board(cur matrix), row and col(zero position) and depth to keep track
    queue.append([board, row, col, depth])
    #set used to keep track of previous tested places
    visited = set()

    while queue:
        #testing the max length of queue
        maxQueue = max(maxQueue, len(queue))
        node, row, col, depth = queue.popleft()
        #chanes board to a single 9 char string, to be saved into visited set
        nodeString = boardToString(node)
        visited.add(nodeString)
        maxNodes += 1

        if atGoalState(node):
            printResults(depth, maxNodes, maxQueue)
            return 
        for dc, dr in directions:
            #dc and dr, are temporary holders for directions, used to calculate possible places zero can move
            tempRow = dr+row
            tempCol = dc+col
            #checks if out of bounds
            if 0 <= tempRow <= 2 and 0 <= tempCol <= 2:
                #copys board and swtiches the zero place with another number
                boardCopy = copy.deepcopy(node)
                boardCopy[row][col] = node[tempRow][tempCol]
                boardCopy[tempRow][tempCol] = 0
                """print()
                print("before", node)
                print("swtichable at", tempRow, tempCol)
                print("after", boardCopy)"""
                boardCopyString = boardToString(boardCopy)
                #if the board is valid and hasn't been tested, it is added to the visted set and appened as a possible solution
                if boardCopyString not in visited:
                    queue.append([boardCopy, tempRow, tempCol, depth+1])
       
#changes matrix/board to a string for vistied set
def boardToString(board):
    string = ''
    for r in range(3):
        for c in range(3):
            string += str(board[r][c])
    return string

#this method finds the zero/missing spot in the matrix and returns the position in row and column
def findZero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                row = i
                col = j
    return row, col

#compares current state with final state returns True if they match
def atGoalState(board):
    goal_board = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    return True if board == goal_board else False
    
#printing results
def printResults(depth, maxNodes, maxQueue):
    print("Soultion found!")
    print()
    print("Depth size of Tree:", depth)
    print("Max expaneded nodes: ", maxNodes)
    print("Max Queue size:", maxQueue)

#call to main
main()