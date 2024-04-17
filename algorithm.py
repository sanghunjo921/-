### 

def destroyBuildings(board, skill):
    answer = 0
    affected = []
    n = len(board)
    m = len(board[0])

    for _ in range(n+1):
        affected.append([0] * (m+1))


    for skill_type, sr, sc, er, ec, degree in skill:
        degree = degree if skill_type == 2 else -degree
        affected[sr][sc] += degree
        affected[sr][ec+1] += -degree
        affected[er+1][sc] += -degree
        affected[er+1][ec+1] += degree

    for i in range(1, n):
        for j in range(m):
            affected[i][j] += affected[i-1][j]
    
    for j in range(1, m):
        for i in range(n):
            affected[i][j] += affected[i][j-1]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += affected[i][j]
            answer += 1 if board[i][j] > 0 else 0
    
    
    return answer


board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(destroyBuildings(board, skill))