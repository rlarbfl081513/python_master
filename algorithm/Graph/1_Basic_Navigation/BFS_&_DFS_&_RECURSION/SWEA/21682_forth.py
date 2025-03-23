import sys
sys.stdin = open("input.txt")

# 숫자는 스택에 넣는다
# 연산자를 만나면 스택의 숫자 두개를 꺼내 더하고 결과를 다시 스택에 넣음
# 항상 코드의 마무리는 '.'이다


# # 큐로 풀기 + eval 사용
# eval을 사용하면 1+2+3같은 문자열을 연산해주기에, 인풋으로 숫자든 연산자든 다 문자열로 받아서 사용함
# 그런데 eval에 의한 결과값은 int가 된다는 점을 유의
# from collections import deque
#
# def que():
#     global q_list,q
#
#     while q:
#         some = q.popleft()
#
#         if some == '.':
#             return print(f'#{tc} {" ".join(q_list)}')
#
#         # 아래처럼 써도 상관은 없지만 더 가독성과 최적화를 하자면
#         # if some != '-' and some != '/' and some != '*' and some != '+' and some != '.':
#         if some not in '-+/*.':
#             q_list.append(some)
#         else:
#             # 문제 조건에 의해 /는 //로 바꿔야함
#             if some == '/':
#                 some = '//'
#
#             if len(q_list) < 2:
#                 return print(f'#{tc} error')
#
#             new = [q_list.pop()]+[q_list.pop()]
#             # 팝으로 가져오면 원래 들어간 순서랑 반대로 나오니까, 뒤집어서 계산함
#             # 안그러면 3-4가 되어 -1이라는 음수가 나오게됨
#             new.reverse()
#
#             # 초기 인풋에서 받아온 숫자를 넣을때는 잘되다가 앞에서 계산된 값들로 계산할때 문제가 생긴 이유는
#             # 아래 코드를 통과하면 int로 되어 리스트에 들어가기에 문제 발생
#             # q_list.append(eval(some.join(new)))
#             # 아래처럼 연산한 값을 다시 문자열로 바꿔서 넣어줘야 다시 연산하려고 할때 아래 코드에서 문제가 없음
#             q_list.append(str(eval(some.join(new))))
#
#
# t = int(input())
# for tc in range(1,1+t):
#      q = deque(list(input().split()))
#      q_list = []
#      que()


# ## 문자열 수식을 실제로 계산하기위해서는???
# # 문자열 수식을 실제로 계산하려면 eval() 사용
# q = [1,2,3]
# jj = '-'
#
# # 아래처럼 쓰면 jj가 그냥 그 자체로 들어가버림 -> 1jj2jj3
# # result = eval("jj".join(map(str,q))
#
# # 아래와 같이 써야함. 변수 jj를 문자열 포맷안에서 값으로 써야함
# result = eval(jj.join(map(str,q)))
#
# print(result)



# # 큐로 풀기 + eval 사용안하고 -> if문으로 경우에 따른 연산을 각각하게 만듦
# from collections import deque
#
# def que():
#     global q_list,q
#
#     while q:
#         some = q.popleft()
#
#         if some == '.':
#             return print(f'#{tc} {" ".join(map(str,q_list))}')
#
#         if some not in '-+/*.':
#             q_list.append(int(some))
#         else:
#
#             if len(q_list) < 2:
#                 return print(f'#{tc} error')
#
#             b = q_list.pop()
#             a = q_list.pop()
#
#             if some == '+':
#                 q_list.append(a + b)
#             elif some == '-':
#                 q_list.append(a - b)
#             elif some == '*':
#                 q_list.append(a * b)
#             elif some == '/':
#                 q_list.append(a // b)
#
#
# t = int(input())
# for tc in range(1,1+t):
#      q = deque(list(input().split()))
#      q_list = []
#      que()



# # 스택으로 풀기
# # 스택으로는 popeft가 안되기에 리스트를 뒤집어서 pop해줘야함
#
# def stack():
#     global for_stack,stack_list
#     # reversed로 하는거 해봄 그냥
#     # stack_list.reverse()
#     li = list(reversed(stack_list))
#
#     while li:
#         some = li.pop()
#
#         if some == '.':
#             return print(f'#{tc} {" ".join(map(str,for_stack))}')
#
#         if some not in '-+/*.':
#             for_stack.append(int(some))
#         else:
#             if len(for_stack) < 2:
#                 return print(f'#{tc} error')
#
#             b = for_stack.pop()
#             a = for_stack.pop()
#
#             if some == '+':
#                 for_stack.append(a + b)
#             elif some == '-':
#                 for_stack.append(a - b)
#             elif some == '*':
#                 for_stack.append(a * b)
#             elif some == '/':
#                 for_stack.append(a // b)
#
#
# t = int(input())
# for tc in range(1,1+t):
#      stack_list = list(input().split())
#      for_stack = []
#      stack()




# 재귀로 풀기

def stack(list_chan):
    global for_stack

    some = list_chan.pop()

    if some == '.':
        return print(f'#{tc} {" ".join(map(str,for_stack))}')

    if some not in '-+/*.':
        for_stack.append(int(some))
    else:
        if len(for_stack) < 2:
            return print(f'#{tc} error')

        b = for_stack.pop()
        a = for_stack.pop()

        if some == '+':
            for_stack.append(a + b)
        elif some == '-':
            for_stack.append(a - b)
        elif some == '*':
            for_stack.append(a * b)
        elif some == '/':
            for_stack.append(a // b)

    stack(list_chan)


t = int(input())
for tc in range(1,1+t):
     stack_list = list(input().split())
     for_stack = []
     stack_list.reverse()
     stack(stack_list)
