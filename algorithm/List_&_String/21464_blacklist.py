

# 7:33
# 블랙리스트 정보를 가지고 아파트에 일반시민과 블랙리스트 몇명인지 봐라

# ## 시간초과라고함
# t = int(input())
# for tc in range(1,1+t):
#     h,w = map(int,input().split())
#     aprt_li = []
#     for i in range(h):
#         aprt_li.extend(list(map(int,input().split())))
#     # 아파트 주민 이름은 숫자로 주어짐(중복된 값 존재 가능)
#     black = []
#     bh, bw = map(int, input().split())
#     for i in range(bh):
#         black.extend(list(map(int,input().split())))
#
#     cnt = 0
#     # for i in black:
#     #     # count는 허용하지 않는 라이브러리라고 함
#     #     # cnt += aprt_li.count(i)
#
#     for i in black:
#         for j in aprt_li:
#             if i == j:
#                 cnt += 1
#
#     print(f'#{tc} {cnt} {h*w - cnt}')


## 이것도 시간초과라고함
# t = int(input())
# for tc in range(1,1+t):
#     h,w = map(int,input().split())
#     aprt_li = []
#     for i in range(h):
#         aprt_li.extend(list(map(int,input().split())))
#     # 아파트 주민 이름은 숫자로 주어짐(중복된 값 존재 가능)
#     black = []
#     bh, bw = map(int, input().split())
#     for i in range(bh):
#         black.extend(list(map(int,input().split())))
#
#     cnt = 0
#     for j in aprt_li:
#         if j in black:
#             cnt += 1
#
#     print(f'#{tc} {cnt} {h*w - cnt}')

#
# t = int(input())
# for tc in range(1,1+t):
#     h,w = map(int,input().split())
#     aprt_li = []
#     for i in range(h):
#         aprt_li.extend(list(map(int,input().split())))
#     # 아파트 주민 이름은 숫자로 주어짐(중복된 값 존재 가능)
#     black = []
#     bh, bw = map(int, input().split())
#     for i in range(bh):
#         black.extend(list(map(int,input().split())))
#
#     cnt = 0
#     black = set()
#
#     for j in aprt_li:
#         if j in black:
#             cnt += 1
#
    # print(f'#{tc} {cnt} {h*w - cnt}')

## 금기륜 강사님 코드
T = int(input())

for tc in range(1, T + 1):
    h, w = map(int, input().split())
    apartments = [list(map(int, input().split())) for _ in range(h)]

    bh, bw = map(int, input().split())
    black_list = [list(map(int, input().split())) for _ in range(bh)]

    # 1. 블랙리스트 체크리스트
    dat = [0] * 100001

    # 2. 체크리스트에 블랙리스트 여부를 체크
    for i in range(bh):
        for j in range(bw):
            target = black_list[i][j]  # 블랙리스트 1명 씩
            dat[target] = 1  # 여부 체크

    # 3. 아파트 주민들을 확인
    black_cnt = 0
    for i in range(h):
        for j in range(w):
            target = apartments[i][j]  # 확인하고자 하는 사람
            if dat[target] == 1:  # 만약 블랙리스트라면
                black_cnt += 1

    print(f'#{tc} {black_cnt} {(h * w) - black_cnt}')
