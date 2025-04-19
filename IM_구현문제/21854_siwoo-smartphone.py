import sys
sys.stdin = open("input.txt")


# 6:43

# 1번 상태 : 겹치는 영역 존재
# 2번 상태 : 겹치는 선만 존재
# 3번 상태 : 겹치는 점만 존재
# 4번 상태 : 아무것도 만나지 않음

# 주어지는 두개의 사각형의 끝점을 이용해 사각형을 그려 상태를 파악하라

# 1번 방식. 2차배열로 직접 그리면서 겹치는 부분 구하기
t = int(input())
for tc in range(1,1+t):
    a_s_x1, a_s_y1, a_e_x1, a_e_y1 = map(int,input().split())
    b_s_x1, b_s_y1, b_e_x1, b_e_y1 = map(int, input().split())

    # 전체 배열은 0~1000가 범위니까 하나의 큰 캔버스를 그려놓음
    arr = [[0]*1001 for _ in range(1001)]

    # 첫번째 사각형의 범위는 1로 칠하기
    for i in range(a_s_x1,a_e_x1+1):
        for j in range(a_s_y1, a_e_y1 + 1):
            arr[i][j] = 1

    # 두개의 사각형이 겹치는 부분의 개수
    cnt = 0
    # 두개의 사각형이 겹치는 y x의 좌표를 각각 set으로 받음
    tow_point_y= set()
    tow_point_x = set()

    # 두번째 사각형의 범위로 칠하기
    for i in range(b_s_x1,b_e_x1+1):
        for j in range(b_s_y1, b_e_y1 + 1):
            # 이미 첫번째 사각형이 칠했던 곳이라면
            # 겹치는 카운트 세기 + yx좌표 넣기
            if arr[i][j] == 1:
                cnt += 1
                tow_point_y.add(i)
                tow_point_x.add(j)


    # 겹치는게 하나도 없을때
    if cnt == 0:
        print(f'#{tc}',4)
    # 겹치는게 한개의 점 일떄
    elif cnt == 1:
        print(f'#{tc}',3)
    # 만약 겹치는 좌표를 넣었던 set의 길이가 y나 x가 1이라면 -> 한 줄로 겹쳤언다는 거임
    elif len(tow_point_y) == 1 or len(tow_point_x) == 1:
        print(f'#{tc}', 2)
    # 아니면 면으로 겹쳤었다는거
    else:
        print(f'#{tc}', 1)



## 2번 방식. 더 짧은 방식 _최상인쓰 코드
T = int(input())
for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    new_x1 = max(x1, x3)
    new_y1 = max(y1, y3)
    new_x2 = min(x2, x4)
    new_y2 = min(y2, y4)

    width = new_x2 - new_x1
    height = new_y2 - new_y1

    if width > 0 and height > 0:
        print(f"#{tc} 1")
    elif width == 0 and height > 0 or height == 0 and width > 0:
        print(f"#{tc} 2")
    elif width == 0 and height == 0:
        print(f"#{tc} 3")
    else:
        print(f"#{tc} 4")
