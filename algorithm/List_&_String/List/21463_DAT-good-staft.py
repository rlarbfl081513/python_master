import sys
sys.stdin = open("input.txt")

# h*w 크기의 출입명단이 있음
# 한 사람당 최대 200회 등장 가능
# 출근 횟수가 가장 많은 사원번호 출력 --> 여러명이면 사원번호가 작은 사람 출력


# ## 런타임 에러 났던 코드 수정
# ## 원인 : 10000001 길이의 리스트를 순회하고 순서바꾸고 하는 코드가 너무 많았어서 그랬음
# ## 해결 : 복잡한 과정 다 뺴고 그냥 리스트 순회하는거 한번만해서 최대 출근횟수의 사원번호 구하게 함

## 아 근데 이 방법도 너무 오래걸리는게 그냥 냅다 10000001 길이의 리스트를 만들어버려서 오래걸림
## ---> 인풋으로 받는 사원번호 중 가장 큰 번호를 기준으로 dat 리스트 범위를 제한하는게 좋을듯
t = int(input())
for tc in range(1,1+t):
    h,w = map(int,input().split())

    # DAT를 위한 리스트
    DAT_person = [0]*10000001

    # 입력 받으면서 바로 리스트에 출근횟수 카운트하기
    for _ in range(h):
        li = list(map(int,input().split()))
        for item in li:
            DAT_person[item] += 1

    # 최대 출근횟수
    max_go = 0
    # 최대로 출근한 사원의 번호
    max_person = 0
    # 리스트를 돌면서 가장 출근을 많이 한 횟수와 동시에 가장 사원번호가 작은 사람 찾기
    for i in range(1,10000001):
        if DAT_person[i] > max_go:
            max_go = DAT_person[i]
            max_person = i
        # 최대 출근횟수가 동일하다면 더 작은 사원번호 가진 사람으로 바꾸기
        elif max_go == DAT_person[i] and max_person > i:
            max_person = i

    print(f'#{tc} {max_person}')




    ## 야야 이건 아니다 규리야
    # 뭔가 더 빨리 찾을수 있지 않을까 해서.
    # 1. 튜플 리스트를 만들고 sort를 해서 출근횟수 순으로 나열 후
    # 2. 가장 뒤에 있는 사람의 출근횟수를 기준으로 그 사람보다 더 작은 사원번호를 가진 사람이 있는지를 확인하게 하는 거였음
    # --> 그런데 이를 위해 리스트를 순회와 재배열 등 너무 시간 많이 사용함 --> 리스트의 길이가 '10000001'이 지경이라서 바로 런타임 에러
    # for i in range(h):
    #     for j in range(w):
    #         person[arr[i][j]] += 1
    #
    # max_li = []
    # for k in range(len(person)):
    #     if person[k] > 0:
    #         # 몇번 출근인지 & 사원번호
    #         max_li.append((person[k],k))
    #
    # max_li.sort()
    # max_li = max_li[::-1]
    # min_per = max_li[0][1]
    # new_person_num = []
    # # 많이 출근한 순서대로 했으니까 출근횟수가 같으면서 사원번호가 작은 경우를 구하는
    # for a,b in max_li:
    #     if max_li[0][0] == a:
    #         new_person_num.append(b)
    # new_person_num.sort()
    # print(f'#{tc} {new_person_num[0]}')




# ## 명현오빠 코드
# ## 딕셔너리로 사원번호(키)와 출근횟수(벨유) 정리
# T = int(input())
# for case in range(T):
#     H, W = map(int, input().split())
#     my_map = [list(map(int, input().split())) for _ in range(H)]
#     my_dict = {}
#     # 사원번화와 출근횟수를 딕셔너리고 정리
#     for i in range(H):
#         for j in range(W):
#             my_dict[my_map[i][j]] = my_dict.get(my_map[i][j], 0) + 1
#
#     print(my_dict)
#     # 최대 출근횟수를 위한 초기값
#     max_v = 0
#     # 최대로 출근한 사원번호를 받을 코드
#     answer_key = None
#     # 딕셔너리를 돌면서 최대로 출근한 사람중 가장 사원번호가 작은 사원 찾기
#     for key, value in my_dict.items():
#         if value > max_v:
#             max_v = value
#             answer_key = key
#         elif value == max_v:
#             if answer_key > key:
#                 answer_key = key
#
#     print(f"#{case + 1} {answer_key}")