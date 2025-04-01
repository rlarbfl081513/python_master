import sys
sys.stdin = open("input.txt")

# 16*16 행렬의 미로
# 읜색은 길 노랑은 벽
# 0,0에서 부터 만들어지고, 1,1에서 시작 --> 도착점은 13,13 --> 길이 있는지 푸는 문제
# 2 가 출발점이고 3이 도착점


# 기본 유니온파인드 코드
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# 결함시키는
def union(x,y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:  # 사이클 방지
        return

    # 그냥 일정한 규칙으로 연결하려고 이렇게 쓴거임
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y



t = 10
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(16)] # 문자열인 숫자를 정수로 바꿔줘야 함수에서 숫자마다 ''안쒸워줘도돼서 편함
    # for row in arr:
    #     print(row)
    parents = [i for i in range(16)]
    # print()
    # print(parents)

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 0:
                if find_set(i) != find_set(j):
                    union(i,j)

    if parents[2] == parents[3]:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',-1)
