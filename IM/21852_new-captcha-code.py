import sys
sys.stdin = open("input.txt")

# n개 길이의 샘플이 주어진다
# k개 길이의 패스코드가 주어진다
# 샘플에서 패스코드를 순차적으로 만들수 있는지 검증해야한다 -> 가능하면 1 출력, 불가능하면 0 출력
# 0~9 사이 정수를 줌


def code_make(start):
    global sample,passcode,k,res

    # 패스코드와 같은 걸 만들 빈 리스트
    new = []

    # new리스트와 패스코드와의 인덱스를 비교하면서, 같으면 넣기
    for i in range(start,len(sample)):
        if sample[i] == passcode[len(new)]:
            new.append(sample[i])
            # 만약 new와 패스코드가 같아지면 res 1로 바꾸고 리턴
            if new == passcode:
                res = 1
                return


t = int(input())
for tc in range(1,1+t):
    n,k = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))

    # 패스코드와 같은 코드를 생성했는지 확인하는 플래그
    res = 0

    # 샘플코드에서 생성가능 여부를 확인할수 있는 인덱스 범위 제한하기
    limit_idx = len(sample)-len(passcode)

    # 포문을 돌리면서, 시작점을 재귀로 돌리면서 가능한 경우가 있는지 보기
    for i in range(limit_idx):
        code_make(i)
        if res == 1:
            print(f'#{tc} {res}')
            break
        elif i == limit_idx-1 and res == 0:
            print(f'#{tc} {res}')

