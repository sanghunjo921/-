### 2024 Naver 공채 문제 1번 

def findHappyPlants(emotions, orders):

    saved_emotions = emotions[:]
    results = []
    
    for o in range(len(orders)):
        num_plants = 0
        

        for e in range(len(emotions)):

            if emotions[orders[o]-1] > 0:
                emotions[orders[o]-1] = saved_emotions[orders[o]-1]
            
            if emotions[e] > 0 and e != orders[o]-1:
                emotions[e] -=1

            if emotions[e] > 0:
                num_plants += 1
        results.append(num_plants)

    return results
            
                
# emotions = [5,5,5]
# orders = [1,2,1,2,3]

# emotions = [5,5,5]
# orders = [1,2,1,2,1]

emotions = [2,1,3,4,3]
orders = [2,2,2,2,5,5,5]


# emotions = [2,3,1,2]
# orders = [3,1,2,1,4,1]
print(findHappyPlants(emotions, orders))

