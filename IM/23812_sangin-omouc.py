import sys
sys.stdin = open("input.txt")


# 바둑판은 19*19
# 1~19번으로 번호가 붙음
# 바둑알이 연속으로 5개가 이어지면 그 색이 이기는 거임, 가로 세로 대각선
# 6알 이상이면 이긴거 아님
# 인풋으로 이긴건지 진건지 승부결정 안났는지 판단
# 1 : 검으색, 2:흰색, 0:빈자리
# 출력 : 테케번호, 승패여부, 결정난 좌표,  결정안났으면 'PLAYING'출력
# 가장 왼쪽,상단에 있는 바둑알이 출력될 알

delta = [(0,1),(1,0),(1,1)]

def omoc(game):
    for i in range(19):
        for j in range(19):
            if game[i][j] == 1:
                new = []

                # 델타로 우,우하,하 방향으로 보면서 검은돌 찾기
                for idx in range(3):
                    ny,nx = i+delta[idx][0], j+delta[idx][1]
                    if 0 > ny or 19 <= ny or 0 > nx or 19 <= nx:
                        continue

                    # 주변에 검은돌 있으면 델타방향과 좌표 넣기
                    if game[ny][nx] == 1:
                        new.append((idx,(ny,nx)))

                # 델타 다 돌면 이제, 딕셔너리에 넣은거로 -> 해당 방향을 따라 쭉 탐색하게 하기
                for i in range(len(new)):
                    new_start_delta, new_start = new[i]
                    new_y,new_x = new_start[0], new_start[1]
                    while True:




t = int(input())
for tc in range(1,1+t):
    arr = [list(map(int,input().split())) for _ in range(19)]

    omoc(arr)