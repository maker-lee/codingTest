'''p314 만들 수 없는 금액
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하자

N = 5
a = [3,2,1,1,9] 
답은 8원

N는 1000이하의 자연수

N=3
a=[3,5,7]
답은 1원
'''

import itertools

N = 3
a = [3,5,7]
# #nP1 ~ nPn

# # 작은수로 나열한다.
# # 1이 없으면 1을 반환한다

lst = []
for i in range(1,N+1) :
    num_list = list(map(sum,(itertools.combinations(a,i))))
    lst.append(num_list)
lst = sorted(set(itertools.chain.from_iterable(lst)),reverse=False) #[3, 5, 7, 8, 10, 12, 15]
print(lst)

cnt = 1
for j in range(len(lst)) :
    if lst[j] == cnt :
        cnt += 1
    else :
        print(cnt)
        break
    

# 책 풀이 

# n = 5
# data = [3,2,1,1,9]
# #data = list(map(int,input().split))
# data.sort() # 최소값을 구하므로 작은 숫자로 정렬한다. 
# # print(data)  # [1, 1, 2, 3, 9]

# coin = 1 #최소값을 구하므로 1부터 +1 씩 늘린다. 
# for i in data : # 가진 숫자들을 하나씩 꺼내서 더할 예정
#     if coin < i :
#         break
#     coin += i # 1+1, 2+1, 3+2, 5+3
# print(coin)




'''볼링공 고르기
A,B가 서로 무게가 다른 볼링공을 고르려고 한다. 경우의 수를 고르세요
N = 볼링공 개수
공의 번호는 1번부터 N번까지다
공의 무게는 1~M까지 자연수다

N=5
M=3
1,3,2,3,2 kg
공의 번호는 1,2,3,4,5

볼링공의 조합은 8가지다. 
1,2 1,3 1,4 1,5 2,3 2,5 3,4 4,5 조합 
1,3 1,2 1,3 1,2 3,2 3,2 2,3 3,2 kg 

예시 2
N=8
M=5
1 5 4 3 2 4 5 2 
답 25 
'''


n = 3
m = 5
ball = [1,3,2,3,2]
# n, m = map(int, input().split()) 
# ball = list(map(int, input().split()))

count = 0 # 총 경우의 수 = 0으로 초기화

for i in itertools.combinations(ball, 2) : # 공 2개 고르는 모든 조합 
    #print(i) #(1, 3),(1, 2),(1, 3),(1, 2),(3, 2),(3, 3),(3, 2),(2, 3),(2, 2),(3, 2)
	if i[0] != i[1]: # 위의 조합중에서 무게가 같지 않은 것만 카운팅한다. 
		count += 1
print(count)




'''무지의 먹방 라이브
회전판에 N개의 음식이 있다. 
음식에는 1부터 N까지 번호가 붙어있다
마지막 번호의 음식을 먹으면 다시 1번으로 돌아온다
무지는 음식을 1초간 먹는다.
남은건 돌아올 때 먹는다. 
회전판이 도는 시간은 계산하지 않는다. 

방송시작 K초후에 방송이 중단된다. 몇번부터 먹어야 하는가

각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times
네트워크 장애가 발생한 시간 K초가 매개변수로 주어진다.
몇번부터 먹어야 하는자?
단, 만약 더 섭취할 음식이 없으면 -1을 반환한다.

food_times는 1~2000사이, 원소는 1~1000 이하, k는 1이상 2,000,000이하의 자연수'''


# 1초 -> 2,1,2 1번먹음
# 2초 -> 2,0,2 2번먹음
# 3초 -> 2,0,1 3번먹음 
# 4초 -> 1,0,1 1번먹음
# 5초 -> 1,0,0 2번없어서 3번먹음 
# 이제 먹을건 1번 



k = 5 # 네트워크 돌아간 초 = 무지가 먹은 횟수 
food_times = [3,2,2] # 음식별 먹는데 걸리는 초 

i = 0
cnt = 1
while True :  
    try :
        print(i+1,'번째 음식 차례',food_times[i],'입 남음')
        if food_times[i] == 0 :
            print('0이라 먹을게 없어서 다음 음식으로 넘어갑니다')
            i += 1 # 먹을게 없으면 그 다음 음식으로 간다. 
            continue
        food_times[i] -= 1 # 한번 먹을 때마다 -1씩 해줌        
        print('남은 분량',food_times[i],'입')
        i += 1
        cnt += 1 # 무지가 먹었다.
        if k < cnt :
            break  
        
    except :
        i = 0 # 만약 3번 음식까지 먹었으면 다시 1번 음식으로 돌아가라 
        print('첫번째 음식으로 돌아갑니다')

while True :
    try :
        if sum(food_times) == 0 : # 더 이상 먹을 음식이 없으면
            print(-1) # -1을 반환한다. 
            break
        elif food_times[i] == 0:
            i += 1 
        else :
            print(i+1,'번째 음식 차례')
            break
    except :
        i = 0
        continue



        
    