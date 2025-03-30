import sys
sys.stdin = open("input.txt")
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 기준 정렬, 같으면 시작 시간 기준
arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for start, end in arr:
    # end_time은 이전 회의의 끝시간으로 다음회의 시작시간과 비교하는 것
    if start >= end_time:
        cnt += 1
        # 끝 시간 갱신하는 코드
        end_time = end

print(cnt)
