# 스택 기본 문제

# ### 괄호의 순서를 보는 문제
# # () [] 이런식으로 연속되는 형태로 괄호가 열리고 닫히는 경우만 인정하는 문제임
# # -> (([))] 이런 형태는 괄호의 짝이 다 있는거긴 하지만 () [] 이런식으로 열리고 닫히는게 아니니까 틀림거임
#
def stack():
    for i in arr:

        if i == '(':
            new.append(i)
        elif i == ')' and new[-1] == '(':
            new.pop()
        elif i == '[':
            new.append(i)
        elif i == ']' and new[-1] == '[':
            new.pop()
        elif i == '{':
            new.append(i)
        elif i == '}' and new[-1] == '{':
            new.pop()
        elif i == '<':
            new.append(i)
        elif i == '>' and new[-1] == '<':
            new.pop()
        elif i != new[-1]:
            print(f'#{tc}', 0)
            return

    if len(new) != 0:
        print(f'#{tc}',0)
    else:
        print(f'#{tc}', 1)

t = 10

for tc in range(1,1+t):
    n = int(input())
    arr = list(input())
    new = []
    stack()



### 괄호들의 짝이 맞게 있는지 없는지만 확인하는 문제였다면
# 열리고 닫히는 각각의 괄호의 개수가 똑같으면 짝이 다 맞는거임

def stack():
    a_open = arr.count('(')
    a_close = arr.count(')')
    new.append((a_open,a_close))

    b_open = arr.count('[')
    b_close = arr.count(']')
    new.append((b_open, b_close))

    c_open = arr.count('{')
    c_close = arr.count('}')
    new.append((c_open, c_close))

    d_open = arr.count('<')
    d_close = arr.count('>')
    new.append((d_open, d_close))

    for a, b in new:
        if a != b:
            print(f'#{tc}',0)
            return

    return print(f'#{tc}',1)


t = 10

for tc in range(1,1+t):
    n = int(input())
    arr = list(input())
    new = []
    stack()