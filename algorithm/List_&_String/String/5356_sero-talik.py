import sys
sys.stdin = open("input.txt")

## 문제
# 영어 대문자부터 소문자 숫자 0~9
# 놓인 단어들을 수평으로 읽다가 수직으로 읽는다
# 빈공간은 그냥 읽는다. 무시하고서
# 세로로 읽은 순서대로 다시 나열
# 5개의 문자를 준다


for tc in range(1,1+int(input())):
    arr = []
    max_len = 0

    for i in range(5):
        arr.append(list(input()))
        if len(arr[i]) > max_len:
            max_len = len(arr[i])

    for row in range(5):
        arr[row] = arr[row] + ['*']*(max_len-len(arr[row]))

    # for row in arr:
    #     print(row)

    # print(max_len)
    new = []
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] =='*':
                continue
            new.append(arr[j][i])
    print(f'#{tc}',"".join(new))