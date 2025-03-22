import sys
sys.stdin = open("input.txt")

# ( 굳이 동맹 나라의 정보를 다 바꿀 필요없이, 대표자만 정하고 그것만 바꾸게 하면되는 거임)
# 1-1. 동맹 시 같은 집합내의 모든 나라의 인구 수 바뀌지 않음
#      -> 인구를 다 바꿀 필요는 없으니까, 그냥 제일 인구많은 나라를 계속 대표자로 선정해서 그 나라 인구수만 업데이트함
# 1-2. 집합 대표의 인구수를 바꾸게 만듦
# 2.   전쟁 시 각 나라의 인구수가 같을 때 --> 둘다 죽는 코드 만듦
# 3.   대표자의 숫자가 큰 나라를 집합의 대표로 하고 있음 -> 인구수가 많은 나라가 대표가 되게

# (추가)
# 테케 1개가 틀렸던게 이거인줄 알았지만 아님---> 그냥 전쟁함수에서 집합의 대표번호 인구수를 부르지 않아서 문제였음
# --> 동맹 중간에 전쟁이 일어나서 멸망한 나라가 있고, 다음에 동맹을 하려는데 멸망한 나라랑 동맹하려고 하면..??안되게 해야지...이게 문제였다..
# 아래는 동맹 중간에 전쟁 일어나는 테케 만든거임
# alliance A C
# alliance F C
# war D A
# alliance D B
# alliance A F

def find(x):

    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def alliance(x, y):
    global parents

    ref_x = find(x)
    # 아래처럼 써야 자신이 속한 집합의 총 인구수를 전달하는 거임
    x_peo = people[ref_x]

    # 대표자 번호는 아래가서 바꿀거니까 여기서는 불필요한 코드
    # parents[x] = ref_x

    # 아래처럼 쓰면 대표자를 찾아놓고도 원래 자신의 인구수를 가져옴
    # 그게 아니라 자기가 속한 집합의 전체 인구 수를 전달해야하는거임
    # x_peo = people[x]

    ref_y = find(y)
    y_peo = people[ref_y]

    # 만약 대표자가 같으면, 이미 동맹국가인거니까 인구수 더하는거 하지말고 리턴해버려
    if ref_x == ref_y:
        return

    # 동맹 -전쟁 -동맹의 과정을 거칠때 -> 이미 멸망한 나라와는 동맹을 맺지 못하게함
    # (그런데 이 코드 없어도 답은 잘나옴 -> 왜냐하면 동맹국의 나라수를 세는게 아니라 인구수가 0이 아닌 나라를 세서 출력하니까)
    # 근데 내가 동맹 맺은 나라들의 수를 세는걸로 출력했으면 필요한 코드임 (같은 대표번호가 2개이상이면 동맹이 있었다는 걸 알 수 있음)
    if x_peo == 0 or y_peo == 0:
        return


    # 두 국가의 인구수를 합하는 그런거
    total_peo = x_peo + y_peo
    # people[ref_y], people[ref_x] = total_peo, total_peo

    # 주어진 번호의 대표자를 바꿔야 -> 집합끼리 합쳐지는 거니까, 아래처럼 써야함
    # 그냥 대표자 나라의 인구수만 바뀌게
    if x_peo > y_peo:
        # 인구수가 많은 나라의 대표번호로 다 통일시키는 거임
        # 그러면 그냥 replace로 다 바꿔버려, 그런데 replace는 문자열에서만 가능하니까...연산하기 힘듦..이 방법 안함
        # parents.replace(ref_y,ref_x)
        # parents[ref_y] = ref_x

        # 제일 위에 대표자로 나의 대표 번호를 바꾼다. 그니까 같은 동맹국이면 다 같은 대표자 번호를 갖게
        # (그 뭐 나중에 타고타고 들어가서 동맹국인지 아닌지 확인하게 하는거 안하려고 넣은거)

        # 인구가 적은 나라의 대표자를 바꿀건데 -> 이때 적은 인구와 미리 동맹했던 나라들도 대표자를 같이 바꾸는 거야
        # 포문으로 하나하나보면서 돌게하면 시간 오래걸릴거 같은데...어쩌라고..그럼 카운트로 세서 하게할까
        # 대표자가 2이면, 2를 대표자로한 나라의 수를 세고 그만큼을 다 바꾸면 포문 그만하게..굳이싶은건가..?
        change_num = parents.count(ref_y)
        cnt = 0
        for i in range(people_num):
            if parents[i] == ref_y:
                parents[i] = ref_x
                cnt += 1
            if cnt == change_num:
                break

        people[ref_x] = total_peo
    else:
        change_num = parents.count(ref_x)
        cnt = 0

        for i in range(people_num):
            if parents[i] == ref_x:
                parents[i] = ref_y
                cnt += 1
            if cnt == change_num:
                break
        people[ref_y] = total_peo



def war(x,y):
    global parents

    # 조건문에서 아래처럼 쓰면, 안됨
    # 내 코드에서는 동맹국 내의 나라들의 대표번호를 다 최상위 대표번호 바꿨기 때문에, 집합의 인구 수를 비교할때는 그 최상위 대표번호의 인구수를 가져와야함
    # people[x] < people[y]
    if people[parents[x]] < people[parents[y]]:
        # 동맹맺은 나라는 하나의 대표자 번호를 가지고 있으니까. 그 대표자 번호 가진 나라 인구 다 죽임
        # 죽어야할 나라의 대표자 번호
        die_par = parents[x]
        for i in range(len(parents)):
            if parents[i] == die_par:
                people[i] = 0

    elif people[parents[x]] > people[parents[y]]:
        die_par = parents[y]
        for i in range(len(parents)):
            if parents[i] == die_par:
                people[i] = 0

    # 전쟁을 하는데 서로 인구수가 같으면 -> 두개의 동맹 다 죽여
    elif  people[parents[x]] == people[parents[y]]:
        die_par_y = parents[y]
        die_par_x = parents[x]
        # 두개의 동맹집합에 속한 나라들이면 다 죽임
        for i in range(len(parents)):
            if parents[i] == die_par_y or parents[i] == die_par_x:
                people[i] = 0


t = int(input())

for tc in range(1, t+1):
    people_num = int(input())
    people = list(map(int,input().split()))

    # [ 0, 1, 2, 3, 4, 5, 6 ]
    parents = [ i for i in range(people_num) ]
    war_alli = []
    for_change = int(input())
    for i in range(for_change):
        war_alli.append(list(map(str,input().split())))

    for i in war_alli:
        if i[0] == 'alliance':
            alliance(ord(i[1])-65,ord(i[2])-65)
        else:
            pass
            war(ord(i[1])-65,ord(i[2])-65)

    ### 0이상의 인구수를 가진 나라의 개수를 세면된다. people이라는 리스트에서 0이상의 값을 가진것을 센다.
    result = people.count(0)
    print(f'#{tc} 인구가 0명이 아닌 나라 수 : {len(people) - result}')

    ### 동맹맺은 나라들을 출력해보자
    # 대표번호가 같은 게 2개 이상이면 동맹이 있었다는 거임 (parents 리스트 내에 같은 번호가 2개 이상)
    # print(parents)

    # set 객체는 **인덱싱([])**이 불가능하기 때문에 "set object is not subscriptable" 오류가 발생
    set_parents = list(set(parents))
    li_result = [[]for _ in range(len(set_parents))]
    # print(parents)
    for i in range(len(set_parents)):
        for j in range(len(parents)):
            if set_parents[i] == parents[j]:
                country = chr(j + 65)
                li_result[i].append(country)

    for i in li_result:
        if len(i) > 1:
            print(f'동맹으로 살아남은 국가 : {" ".join(i)}')


    # 디버깅을 위한 프린트
    # print(people)
    # print(parents)



### input
# 2
# 7
# 10 20 30 40 50 60 70
# 5
# alliance A C
# alliance F C
# alliance D B
# alliance A F
# war D F
# 3
# 38481 86027 89663
# 2
# war A B
# war B C

### output
# 앞의 숫자는 테케 번호
# 1 5
# 2 1