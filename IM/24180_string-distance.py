import sys
sys.stdin = open("input.txt")


# k개의 A를 포함한 부분을 찾고
# A사이의 거리가 가장 긴 값을 출력


def distance(k,arr):
    max_a = 0
    # 일단 계속 움직이다가 개수에 충족하는 만큼 있으면은 그만하고 개수를 반환, 그냥 맥스 값으로 계속해서 업데이트 시키기
    for i in range(len(arr)):
        if arr[i] == 'A':
            cnt = 1
            # a가 아니어도 수는 세야함, a일떄 카운트를 올리는 거고
            for j in range(i+1,len(arr)):
                if arr[j] == 'A' and cnt <= k:
                    cnt += 1
            max_a = max(max_a,cnt)
    return max_a

t = int(input())
for tc in range(1,1+t):
    k = int(input())
    arr = list(input())

    result = distance(k,arr)
    if result == 0:
        print(f'#{tc}',0)
    else:
        print(f'#{tc}', result)
