import sys
sys.stdin = open("input.txt")

# ## 시간초과남!!!!!어쩌라고
# t = int(input())
# for tc in range(1,1+t):
#     a_y,a_x = map(int,input().split())
#     a_arr = [list(map(int,input().split())) for _ in range(a_y)]
#     b_y,b_x = map(int,input().split())
#     b_arr = [list(map(int,input().split())) for _ in range(b_y)]
#
#     # 블랙리스트 2차배열을 1차원배열로 만들기 (아래에서 비교하기 쉬우라고 하는 과정임)
#     new_b = []
#     for row in b_arr:
#         new_b.extend(row)
#
#     # 블랙리스트
#     cnt = 0
#
#     # 일반 시민 리스트를 돌리면서 블랙리스트에 해당하면 카운트 올리기
#     # 여기서 시간초과인가??2차배열 돌면서 리스트에 있는지 없는지 계속 확인하니까????
#     for i in a_arr:
#         for j in i:
#             if j in new_b:  # O(N) 시간,그런데 이걸 2중 for문 안에서 계속 실행하니까, 최악의 경우 시간복잡도는:전체 아파트 주민 수 × 블랙리스트 수
#                 cnt += 1
#
#     # 전체 아파트 주민 숫자에서 블랙리스트 명 수만큼 빼기
#     normal_person = a_y*a_x - cnt
#
#     # 블랙리스트 몇명, 일반 시민 몇명
#     print(f'#{tc}',cnt,normal_person)




## 다른 방법 시도해야돼??????해야지 --- 그냥 블랙리스트는 set으로 바꾸면됨
# new_b를 집합(set) 으로 바꾸면 in 연산이 O(1) 로 줄어들어.

    # 정리
    # - 리스트 → 느림 (O(N))
    #
    # - 집합 → 빠름 (O(1))
    #
    # -- 시간초과 날 땐 리스트를 set으로 바꿔서 확인하자!

t = int(input())
for tc in range(1,1+t):
    a_y,a_x = map(int,input().split())
    a_arr = [list(map(int,input().split())) for _ in range(a_y)]
    b_y,b_x = map(int,input().split())
    b_arr = [list(map(int,input().split())) for _ in range(b_y)]

    # 블랙리스트 2차배열을 1차원배열로 만들기 (아래에서 비교하기 쉬우라고 하는 과정임)
    new_b = set()
    for row in b_arr:
        # 리스트를 추가할떄는 update로 추가하면 extned처럼 추가됨
        new_b.update(row)

    # 블랙리스트
    cnt = 0

    # 일반 시민 리스트를 돌리면서 블랙리스트에 해당하면 카운트 올리기
    # 여기서 시간초과인가??2차배열 돌면서 리스트에 있는지 없는지 계속 확인하니까????
    for i in a_arr:
        for j in i:
            if j in new_b:  # O(N) 시간,그런데 이걸 2중 for문 안에서 계속 실행하니까, 최악의 경우 시간복잡도는:전체 아파트 주민 수 × 블랙리스트 수
                cnt += 1

    # 전체 아파트 주민 숫자에서 블랙리스트 명 수만큼 빼기
    normal_person = a_y*a_x - cnt

    # 블랙리스트 몇명, 일반 시민 몇명
    print(f'#{tc}',cnt,normal_person)