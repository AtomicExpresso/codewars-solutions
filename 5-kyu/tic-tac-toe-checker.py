def is_solved(board):
    cols = [[],[],[]]
    
    for i in range(len(board)):
        x = set(board[i])
        if len(x) == 1:
            return x.pop() if 1 in x or 2 in x else -1
            
        cols[0].append(board[i][0])
        cols[1].append(board[i][1])
        cols[2].append(board[i][2])
    
    for i in range(len(cols)):
        if len(set(cols[i])) == 1: 
            return cols[i][0]
        
    if cols[0][0] == cols[1][1] and cols[0][0] == cols[2][2]: 
        return cols[0][0] if cols[0][0] != 0 else -1
    if cols[0][2] == cols[1][1] and cols[0][2] == cols[2][0]: 
        return cols[0][2]
    
    if 0 in cols[0] or 0 in cols[1] or 0 in cols[2]: 
        return -1
    
    
    return 0
