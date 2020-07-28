def verify(board, sequence, x, y, i):
    #print(board[x][y], x, y)
    letter = board[x][y]
    board[x][y] = i-1
    if i >= len(sequence):
        #print(board)
        board[x][y] = letter
        return True
    for a in range(x-1, x+2, 2):
        if a>=0 and a<len(board):
            if(board[a][y] == sequence[i]):
                #print(a, y, board[a][y])
                state = verify(board, sequence, a, y, i+1)
                if state:
                    board[x][y] = letter
                    return True
    for b in range(y-1, y+2, 2):
        if b>=0 and b<len(board[x]):
            if(board[x][b] == sequence[i]):
                #print(x, b, board[x][b])
                state = verify(board, sequence, x, b, i+1)
                if state:
                    board[x][y] = letter
                    return True
    board[x][y] = letter
    return False

def exists(board, sequence):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if(board[x][y] == sequence[0]):
                #verify if there is the next one
                state = verify(board, sequence, x, y, 1)
                if state:
                    return True
    return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))
