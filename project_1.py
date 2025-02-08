
from collections import deque 
from heapq import heapify, heappush, heappop 
import copy

#these are testing boards that can be used
"""
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
    board = [[1, 2, 3], [4, 5, 0], [7, 8, 6]] #1 depth 
    board = [[1, 2, 3], [0, 4, 5], [7, 8, 6]] #3 depth 123045786
    board = [[4, 1, 3], [0, 2, 6], [7, 5, 8]] #5 depth 413026758
    board = [[5, 4, 2], [3, 0, 6], [7, 8, 1]] #18 depth 542306781
"""

def main():    
    print("welcome to project 1: input 3 numbers for the first row.")
    board = []    
    for i in range(3):
        print("input 3 numbers separated by space!")
        temp = input().split(" ")
        for j in range(3):
            temp[j] = int(temp[j])
        board.append(temp) 
    print()
    print("your board is!", board)
    print("A Star with Manhattan Distance")
    aStar(board, hScoreManhattanDistance) #hScoreManhattanDistance #hScoreMisplacedTile
    print("A Star with Misplaced Tile")
    aStar(board, hScoreMisplacedTile)
    print("Uniform Cost")
    uniformCostSearch(board)

def aStar(board, hScore):
    #directions are used later to simplifying the possible swaps the zero can make
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    depth, maxNodes, maxQueue = 0, 0, 0
    #uses minheap
    heap = []
    #row and col are used to keep location of the zero, reducing having to find the zero every new integration
    row, col = findZero(board)
    #function call to find f-score = h-score+depth(g-score)
    fScore = hScore(board)
    #appending board(cur matrix), row and col(zero position) and depth to keep track
    heappush(heap, [fScore, depth, board, row, col])
    #set used to keep track of previous tested places
    visited = set()

    while heap:
        #testing the max length of queue
        maxQueue = max(maxQueue, len(heap))
        fScore, depth, node, row, col = heappop(heap)
        #changes board to a single 9 char string, to be saved into visited set
        nodeString = boardToString(node)
        visited.add(nodeString)
        maxNodes += 1
        #print("current board being looked at: ", node)
        #print(node)
        if atGoalState(node):
            printResults(depth, maxNodes, maxQueue)
            return 
        for dc, dr in directions:
            #dc and dr, are temporary holders for directions, used to calculate possible places zero can move
            tempRow = dr+row
            tempCol = dc+col
            #checks if out of bounds
            if 0 <= tempRow <= 2 and 0 <= tempCol <= 2:
                #copies board and switches the zero place with another number
                boardCopy = copy.deepcopy(node)
                boardCopy[row][col] = node[tempRow][tempCol]
                boardCopy[tempRow][tempCol] = 0
                boardCopyString = boardToString(boardCopy)
                #if the board is valid and hasn't been tested, it is added to the visited set and append as a possible solution
                if boardCopyString not in visited:
                    fScore = hScore(boardCopy) + depth + 1
                    #print(fScore, hScore(boardCopy), depth)
                    heappush(heap, [fScore, depth + 1, boardCopy, tempRow, tempCol])
                    
    
#function to return hScore
def hScoreManhattanDistance(board):
    #goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #goal state 123456780
    curNum = 1
    score, row, col = 0, 0, 0
    while curNum <= 8:
        for r in range(3):
            for c in range(3):
                if board[r][c] == curNum:
                    tempCol = abs(col-c)
                    tempRow = abs(row-r)
                    score += tempCol + tempRow
                    if col >= 2:
                        col = 0
                        row += 1
                    else:
                        col += 1
                    curNum += 1
    return score

def hScoreMisplacedTile(board):
    curNum = 1
    score = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] != curNum and curNum != 9:
                score += 1
            curNum += 1
    return score

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
        #changes board to a single 9 char string, to be saved into visited set
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
                #copies board and switches the zero place with another number
                boardCopy = copy.deepcopy(node)
                boardCopy[row][col] = node[tempRow][tempCol]
                boardCopy[tempRow][tempCol] = 0
                boardCopyString = boardToString(boardCopy)
                #if the board is valid and hasn't been tested, it is added to the visited set and append as a possible solution
                if boardCopyString not in visited:
                    queue.append([boardCopy, tempRow, tempCol, depth+1])
       
#changes matrix/board to a string for visited set
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
    print("Solution found!")
    print()
    print("Depth size of Tree:", depth)
    print("Max expanded nodes: ", maxNodes)
    print("Max Queue size:", maxQueue)
    print()
#printing function if needed
def printing(board):
    for r in range(3):
        print(''+ str(board[r][0]) + " " + str(board[r][1]) + " " + str(board[r][2]))
        
#call to main
main()
