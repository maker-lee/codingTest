'''
p. 96 숫자 카드 게임 
1. 숫자가 쓰인 카드들이 N(행) * M(열) 형태로 있다
2. 뽑고 싶은 카드가 있는 행을 선택한다
3. 선택한 행에서 가장 낮은 카드를 뽑는다
4. 가장 높은 숫자가 쓰인 카드를 뽑는 사람이 이긴다.

첫째 줄에 N과 M이 공백을 기준으로 하여, 자연수로 주어진다.(1~100)
둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 

게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오 

#예시 1 
N = 3
M = 3 
num_list1 = [3,1,2]
num_list2 = [4,1,4]
num_list3 = [2,2,2]

# # 예시 2
# N = 2
# M = 4
# num_list1 = [7,3,1,8]
# num_list2 = [3,3,3,4]
'''

# 기본 골조 
# 입력받은 숫자들을 하나씩 꺼낸다
# 가장 낮은 수끼리 비교한다
# 낮은 수들 중에 가장 높은 애를 선택한다. 

# 첫행 입력
input_num = []
chioce_low_num = []
num_list = (input('몇행의 몇열을 입력할지 차례로 입력해주세요.'))
M, N = map(int,num_list.split(" "))

# 두번째행 입력
for i in range(M) :
    num_list = (input('숫자를 입력하세요.'))
    input_num.append(list(map(int,num_list.split(" ")))) # 숫자를 입력 받아서 각각 리스트 형태로 담는다. # [[3, 1, 2], [3, 1, 1], [2, 2, 2]]    

# 작은수 뽑기
for j in range(M) :
    chioce_low_num.append(min(input_num[j])) 
choice_num = max(chioce_low_num) # 작은 애들 중 가장 큰 숫자
n = chioce_low_num.index(max(chioce_low_num)) # 2는 몇번째 위치에 있지? 0,1,2할때 2번째요 

# 정답 출력 
print(f'{n}행의 {choice_num}을/를 뽑으세요.')



'''
p99 1이 될때가지
임의의 수 N이 1이 될 때까지 아래 두 과정 중 하나를 반복적으로 선택하여 수행한다.
1. N에서 1을 뺀다
2. N을 K로 나눈다. 
두번째 연산은 N이 K로 나누어 떨어질때만 선택할 수 있다.
N과 K가 주어질 때 1,2 과정을 수행하는 최소 횟수를 구하는 프로그램을 작성하시오. 

예시)
N = 17, K = 4 
1번 - 16
2번 - 8 (16/4)
3번 - 4 (8/4)
-> 전체 과정을 실행한 횟수는 3이 된다. 

N,K는 자연수로 주어지며 공백으로 구분된다. N은 K 보다 크거나 같다.

예시) 
25 5 
출력) 
2
'''
num = input('숫자를 입력하세요.')
N, K = map(int,num.split(" "))
cnt = 0
while N != 1 : 
    if N % K >= 1 : # N을 K로 나눠서 나머지가 1보다 크거나 같으면
        N -= 1 # 방법2를 써라
        cnt += 1
    elif N % K == 0 : # 똑 떨어지면 
        N /= K  # 방법1을 써라 
        cnt += 1
print(cnt,'번')
