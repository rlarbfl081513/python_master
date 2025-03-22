## 문제 설명
# 0-9로 이뤄진 번호 문자열 -> 같은 번호호 붙어있는 쌍들을 소거하고 남은 번호를 비번으로 만듦
# 소거하고 또 쌍이 되면 또 소거


# # 재귀
# def password(num):
#     global n
#
#     # 한번 돌면서 연속되는 수 있는지 보기
#     for i in range(len(num)-1):
#         if num[i] == num[i+1]:
#             num = num[:i] + num[i+2:]
#             return password(num)
#
#         elif i == len(num)-2:
#             return print(f'#{tc} {" ".join(map(str,num))}')
#
# t = 1
# for tc in range(1,t+1):
#     n,num = map(int, input().split())
#     num = list(map(int,str(num)))
#     password(num)


# 테스트
def password(num):
    global n

    # 한번 돌면서 연속되는 수 있는지 보기
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            num = num[:i] + num[i+2:]
            return password(num)

        elif i == len(num)-2:
            return print(f'#{tc} {" ".join(map(str,num))}')

t = 1
for tc in range(1,t+1):
    n,num = map(int, input().split())
    num = list(map(int,str(num)))
    password(num)
