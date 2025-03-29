import sys
sys.stdin = open("input.txt")

def prior(a):
    if a == '+':
        return 1
    elif a == '*':
        return 2

    return 0


def post_fix(arr):
    op_stack = []
    stack = []

    for a in arr:
        if a.isdigit():
            stack.append(a)

        elif a == '(':
            op_stack.append(a)

        elif a == ')':
            while op_stack and op_stack[-1] != '(':
                stack.append(op_stack.pop())
            op_stack.pop()


        else:
            while op_stack and prior(op_stack[-1]) >= prior(a):
                stack.append(op_stack.pop())
            op_stack.append(a)

    while op_stack:
        stack.append(op_stack.pop())

    return stack


def cal(arr):
    stack = []

    for a in arr:
        if a == '+':
            x = stack.pop()
            y = stack.pop()
            res = int(x) + int(y)
            stack.append(res)

        elif a == '*':
            x = stack.pop()
            y = stack.pop()
            res = int(x) * int(y)
            stack.append(res)

        else:
            stack.append(a)

    return stack[0]


T = 1
for t in range(1, T + 1):
    N = int(input())
    arr = list(input())

    math_ex = post_fix(arr)
    result = cal(math_ex)

    print(f'#{t} {result}')