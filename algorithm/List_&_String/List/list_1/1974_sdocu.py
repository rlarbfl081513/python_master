import sys
sys.stdin = open("input.txt")
# 19:14

# 스도쿠는 9*9, 1~9까지 숫자로 이뤄짐
# 겹치는 숫자가 없을때 1 출력, 아니면 0 출력


## 2차배열을 가로와 세로와 작은 사각형으로 나눠서 확인하는 방법은 각각의 함수로 만들어 파악
# 가로세로롤 쪼갠걸 1~9로 이뤄진건지 확인하기
def secon_step(matrix):
    # 1. 한줄씩 차근히 보기, 가로와 세로를 zip 써서 해볼까
    # 한줄씩 끊어와서 오른차순하고

    # 단, sort()는 위험 → sorted() 사용 권장
    # 왜냐하면 sort()는 원본을 바꾸니까 --> 하지만 지금은 함수에 넣기전 2차배열을 복사해서 쓰기때문에 sort()써도됨
    matrix.sort()
    new = set(matrix)
    if len(new) == 9:
        return 1

    return 0


# 2차배열을 가로세로로 쪼개기
def first_step(matrix):
    # 총 9+9+9=27개의 성공이 나오면되는거임
    total = 0
    # 가로로 확인하기
    blank = []
    for row in matrix:
         blank.append(row[::-1])

    for li in blank:
        total += secon_step(li)

    # 세로로 확안하기
    for sero in zip(*matrix):
        sero = list(map(int,list("".join(list(map(str,sero))))))
        total += secon_step(sero)
    # print('2', total)

    return total


def little_square(matrix):
    global cnt

    # 작은 사각형부터 1~9로 채워졌는지 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            new = set()
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    new.add(matrix[a][b])
            if len(new) == 9:
                cnt += 1

    return cnt


t = int(input())
for tc in range(1,1+t):
     arr = [list(map(int,input().split())) for _ in range(9)]
     cnt = 0

     # 작은 사각형부터 1~9로 채워졌는지 확인
     cnt += little_square(arr)
     # 가로세로로 1~9로 채워졌는지 확인
     cnt += first_step(arr)

     if cnt == 9*3:
         print(f'#{tc}', 1)
     else:
         print(f'#{tc}', 0)



## 위와 같은 방식이지만 좀 더 간결한 (출처:명현오빠 코드)
def success(my_matrix):
    # 행검사
    for i in range(9):
        temp_set = set(my_matrix[i])  # 재할당하므로 초기화 필요x
        if len(temp_set) == 9:
            return_value = 1
        else:
            return 0

    # 열검사
    for j in range(9):
        temp_set = set()  # 초기화
        for i in range(9):
            temp_set.add(my_matrix[i][j])
        if len(temp_set) == 9:
            return_value = 1
        else:
            return 0

    # 부분검사 x 9번 -> 노가다 하기 힘드니 range(a,b,3)을 이용
    for part_i in range(0, 9, 3):
        for part_j in range(0, 9, 3):
            # 부분 집합 내부
            temp_set = set()  # 부분집합 할때마다 초기화
            for i in range(part_i, part_i + 3):
                for j in range(part_j, part_j + 3):
                    temp_set.add(my_matrix[i][j])
            if len(temp_set) == 9:
                return_value = 1
            else:
                return 0

    return 1


T = int(input())
for i in range(T):
    my_input_matrix = [list(map(int, input().split())) for _ in range(9)]

    print(f"#{i + 1} {success(my_input_matrix)}")
