### 2023 kakao blind
### 이모티콘 할인행사
### 백트랙킹 
### 이모티콘의 최대 경우의 수는 4^7 탐색 필요 
### 모든 경우의 수를 살펴봐야 하고 할인율 조합이 2차원이기 때문에 dfs 필요
### 모든 경우의 수를 살펴보면서 플러스에 가입할지 이모티콘 구입할지 결정하고 가장 많이 가입하고 가장 많이 파는 경우의 수로 갱신 

from itertools import product 

def solution(users, emoticons):

    register_user_count = 0
    max_price = 0

    discounts = product([10, 20, 30, 40], repeat=len(emoticons)) 
                            
                    
    for discount in discounts:

        user_count, sum_price = 0, 0

        for user in users:
            pay = 0

            for i in range(len(emoticons)):
                if discount[i] >= user[0]:
                    pay += emoticons[i] * (100 - discount[i])/100 
                    

            if pay >= user[1]:
                user_count += 1
            else:
                sum_price += pay

        if(register_user_count < user_count):
            register_user_count = user_count
            max_price = sum_price
        elif (register_user_count == user_count):
            if(max_price < sum_price):
                max_price = sum_price
    
    return [register_user_count, max_price]




users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
# emoticons = [1300, 1500, 1600, 4900]

solution(users, emoticons)
