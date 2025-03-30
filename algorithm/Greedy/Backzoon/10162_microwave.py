# 5585의 거스름돈과 비슷하지만 이번건, 각각의 요소를 몇번 썼는지 출력하는 문제로
# 각 요소에서 나오는 카운트를 총 합의 변수에 들어가기전에 리스트에 어팬드하여 구함

def microwave(second):
    cnt = 0
    time_list = []

    for sec in time:
        cnt_time = second//sec
        time_list.append(cnt_time)
        cnt += cnt_time
        second %= sec


    if second == 0:
        return " ".join(list(map(str,time_list)))
    else:
        return -1


time = [5*60, 60, 10]
n = int(input())
print(microwave(n))