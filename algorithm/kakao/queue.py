### 두 큐의 합 구하기 

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

print(solution(queue1, queue2))