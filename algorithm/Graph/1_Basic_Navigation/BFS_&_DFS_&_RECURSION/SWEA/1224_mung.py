import sys
sys.stdin = open("input.txt")

def trans_middle_back(middle_str, N):
    # 우선 순위. * / + - >> 괄호 안에서도 이 우선순위 적용.
    score = {"*": 2, "/": 2, "+": 1, "-": 1}
    output = []
    stack = []
    for token in middle_str:
        if token.isalnum():  # 피연산자면 출력
            output.append(token)
        elif token == '(':  # 여는 괄호면 push
            stack.append(token)
        elif token == ')':  # 닫는 괄호면 '(' 만날 때까지 pop
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # '(' 제거 (출력 X)
        else:  # 연산자 처리
            while stack and stack[-1] != '(' and score[stack[-1]] >= score[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:  # 남아 있는 연산자 pop
        output.append(stack.pop())
    retun_v = " ".join(output) + " ."  # 끝 알리려고
    return retun_v


def back_calcul(back_str):  # 항상 나누어 떨어지는 케이스만 준다고함 >> 실수화 방지를 위해 //를 사용한다.
    stack = []
    cal_sign = ["+", "-", "*", "/"]
    i = 0
    while back_str[i] != ".":
        if back_str[i] not in cal_sign:
            stack.append(back_str[i])
        else:  # 계산 sign인 경우
            if len(stack) < 2:
                return None  # error
            try:
                i_1 = int(stack.pop())  # i-1
                i_2 = int(stack.pop())  # i-2
                if back_str[i] == "+":
                    stack.append(i_2 + i_1)
                elif back_str[i] == "-":
                    stack.append(i_2 - i_1)
                elif back_str[i] == "*":
                    stack.append(i_2 * i_1)
                elif back_str[i] == "/":
                    if i_1 == 0:
                        return None  # 0으로 나눌 수 없음
                    stack.append(i_2 // i_1)
            except ValueError:
                return None  # 연산자가 아닌 숫자도 아닌 이상한 문자 존재.
        i += 1
    # while이 "."으로 끝난 상태
    if len(stack) == 1:
        return stack[0]
    else:  # 연산이 끝나고 stack이 1개가 아니라면 2개지.
        return None
    # 숫자발견 숫자발견 연산자발견 => 계산 후, return 재귀


T = 1
for case in range(T):
    N = int(input())
    middle_str = list(input())
    print(f"#{case + 1} ", end="")
    back_str = trans_middle_back(middle_str, N)
    # print(back_str)
    if back_calcul(back_str.split()) == None:  # split을 받는 함수였으므로
        print("error")
    else:
        print(back_calcul(back_str.split()))