
# 0~n번 까지 이동
# n번 정류장까지 이동
# 한번 충전으로 최대이동 정류장 수 k개 정해짐
# 충전기 설치된 m개의 정류장 번호 주어짐
# 최소한 몇번의 충전을 해야 종점에 도착할 수 있는지 출력
# 충전기 설치 이상해서 종점에 도착못하면 0을 출력, 출발지에는 항상 충전기 설치되어있느지만 충전횟수에 포함안함

import sys
sys.stdin = open("input.txt")


## 내 코드

# def bus(k,n,m,arr):
#     global new, res
#     # 도착하면 충전횟수 리턴
#     # if 이동해서 도착한 곳 === n
#     # res = 충전횟수
#     # return
#
#     # 일단 출발하고
#     # 가다가 충전 해야하면 먹고
#     # 연료가 부족하지 않는 선에서 가장 멀리 있는 정류장에서 충전을 해야함
#     # 현재 위치에서 갈 수 있는 가장 멀리 있는 정류장 동시에 갈 필요 없으면 안가도 되는데///.......
#     curr_fu = k
#     cnt = 0
#     # 일단 충전소 있으면 다 들어가는 코드 구현
#     pos = 0
#
#     # 0 1 2 3 4 5
#
#     while True:
#         # 현재 위치에 충전소가 있는데 들를 필요가 없으면 그냥 넘어가라는 코드 추가
#         # 아직 연료가 많고 이 연료로 앞의 충전소로 이동할 수 있다면 지금 충전소는 지나가고 다음 정류장의 충전소에서 충전하게 하기
#         for j in range(pos+curr_fu,pos-1,-1):
#             if j == n:
#                 res = cnt
#                 return
              # 가장 멀리 있는 충전 가능한 충전소를 찾는데, 리스트를 돌다가 현재 정류장까지 왔다는건 없다는 거니까 이때 리턴해버리기
#             if j == pos:
#                 return
#             if j in arr:
#                 # 아래 두 코드는 연료가 누적 가능하다고 했을때 필요한 코드
#                     # curr_fu = curr_fu - (j - pos)
#                     # 연료는 누적되는거 아님 최대로 넣을 수 있는 양이 정해짐
#                     # curr_fu = curr_fu + k
#                 # 연료 누적 없이 그때그때 최대k만큼만 충전됨
#                 curr_fu = k
#
#                 cnt += 1
#                 pos += j - pos
#                 break
#
#
# t = int(input())
# for tc in range(1,1+t):
#     # 인풋
#     # k : 한번충전으로 이동할 수 있는 정류장
#     # n : 0부터 n번까지 이동
#     # m : 충전기가 설치된 정류장 수
#     K,N,M = map(int,input().split())
#     # 충전기가 설치된 정류장 리스트
#     ARR = list(map(int,input().split()))
#
#     # 전체 정류장
#     new = list(i for i in range(N+1))
#     # 도착하지 못했을 시를 위한 플래그
#     res = 0
#
#     # 함수 호출과 답 프린트
#     bus(K, N, M, ARR)
#     print(f'#{tc} {res}')




## gpt가 최적화해준 코드

def bus(k, n, chargers):
    # O(1) 탐색을 위한 set
    # 충전소 탐색을 for문으로 도는 거 느림
    charger_set = set(chargers)
    cnt = 0
    pos = 0

    while pos + k < n:
        next_pos = -1
        # 가장 멀리 충전소 찾기
        for i in range(pos + k, pos, -1):
            if i in charger_set:
                next_pos = i
                break
        # 갈 수 있는 충전소가 없다면 0 리턴
        if next_pos == -1:
            return 0
        # 이동한후의 현재 위치
        pos = next_pos
        cnt += 1

    return cnt



t = int(input())
for tc in range(1, t + 1):
    K, N, M = map(int, input().split())
    ARR = list(map(int, input().split()))
    result = bus(K, N, ARR)
    print(f'#{tc} {result}')
