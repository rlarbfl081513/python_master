import sys
sys.stdin = open("input.txt")

# h*w 크기의 출입명단이 있음
# 한 사람당 최대 200회 등장 가능
# 출근 횟수가 가장 많은 사원번호 출력 --> 여러명이면 사원번호가 작은 사람 출력


## 런타임 에러 난 코드/./......
# 너무 리스트가지고 순서 바꾸고 순회하는게 많은가
t = int(input())
for tc in range(1,1+t):
    h,w = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    # print(arr)

    person = [0]*10000001

    for i in range(h):
        for j in range(w):
            person[arr[i][j]] += 1

    max_li = []
    for k in range(len(person)):
        if person[k] > 0:
            # 몇번 출근인지 & 사원번호
            max_li.append((person[k],k))

    # max_li.sort(key=lambda x:x[1])
    max_li.sort()
    # print(max_li)
    # print(person)

    max_li = max_li[::-1]
    # print(max_li)
    min_per = max_li[0][1]
    new_person_num = []
    # 많이 출근한 순서대로 했으니까 출근횟수가 같으면서 사원번호가 작은 경우를 구하는
    for a,b in max_li:
        if max_li[0][0] == a:
            new_person_num.append(b)
    new_person_num.sort()
    print(f'#{tc} {new_person_num[0]}')