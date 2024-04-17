###  2023 kakao 파괴되지 않은 건물 

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

from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    dq1, dq2 = deque(queue1), deque(queue2)
    max_count = len(queue1) * 4

    if sum_q1 == sum_q2:
        return 0
    elif (sum_q1 + sum_q2) % 2 != 0:
        return -1
    

    while True:
        if sum_q1 > sum_q2:
            item = dq1.popleft()
            dq2.append(item)
            sum_q1 -= item
            sum_q2 += item
            answer += 1
        elif sum_q2 > sum_q1:
            item = dq2.popleft()
            dq1.append(item)
            sum_q1 += item
            sum_q2 -= item
            answer += 1
        else:
            break
        if answer == max_count:
            return -1
    return answer
    

# queue1 = [3, 2, 7, 2] 
# queue2 = [4, 6, 5, 1]

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

# queue1= [1, 1]
# queue2= [1, 5]

solution(queue1, queue2)