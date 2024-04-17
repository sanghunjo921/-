from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(set) # 이웃이 여러개라 셋으로 

    ### 이웃들을 더해주기 
    for i, j, w in paths:
        graph[i].add((j,w))
        graph[j].add((i,w))

    intensities = [float('inf')] * (n+1)

    heap = []
    for gate in gates:
        intensities[gate] = 0 
        heappush(heap, (0, gate)) # (intensity, gate) 
    print(heap)

    while heap:
        i, n = heappop(heap) # intensity, gate(현재지점)
        if intensities[n] < i or n in summits: # 더 이상 intensity를 업데이트 할 필요 없음 
            continue
        for j, ji in graph[n]: # 현재 지점에서 이웃과 이웃까지 도달하는 intensity 
            ni = max(i, ji)  # 산봉우리까지 가는 경로동안 가장 큰 intensity를 최소화 해야 하기 때문에 가장 큰 값으로 새로운 intensity 변경 

            if intensities[j] > ni:  # 만약 이웃의 intensity가 새로운 intensity보다 크면 새로운 값으로 변경이 필요함 왜냐하면 해당 지점에 도달하기 위한 intensity
                intensities[j] = ni 
                heappush(heap, (ni, j)) 

    summits = set(summits)

    answer = [-1, float('inf')]

    for summit in sorted(summits):
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[ni]] 



    return answer 


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

print(solution(n, paths, gates, summits))