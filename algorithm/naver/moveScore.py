from collections import deque

def moveScores(cap, k, scores, m):
    upper_bound = deque()
    lower_bound = deque()
    num_affected = 0

    for score in scores:
        if score > k:
            upper_bound.append(score)
        else:
            lower_bound.append(score)

    if (len(lower_bound) == 0): return -1
    
            
    smallest_lower = lower_bound.pop()
    num_affected += 1

    while len(upper_bound) >= m:
        smallest_upper = upper_bound.pop() 
        num_affected += 1

        while smallest_upper > k:

            if smallest_lower >= k:
                smallest_lower = lower_bound.pop()
                num_affected += 1
            
            smallest_lower += 1
            smallest_upper -= 1
            
            
    return num_affected
    

        
# cap = 2000
# k = 1998
# scores = [2000, 2000, 2000, 2000, 1999]
# m = 5
    


# cap = 100
# k = 70
# scores = [95,90, 80, 80, 80, 70, 70, 30, 10]
# m = 4

cap = 100
k = 82
scores = [100,97, 97, 92, 87, 77, 77, 72, 72]
m = 4

moveScores(cap, k, scores, m)