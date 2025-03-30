# 가장 적은 잔돈의 개수를 주게하자

def changed(result):

    cnt = 0  # 잔돈의 개수를 세는
    # 받을 수 있는 가장 큰 단위의 잔돈부터 넣기 시작
    for coin in money:
        # 나누기를 통해 해당 돈으로 얼만큼을 낼수 있는지 판단
        cnt_coin = result // coin
        # 낸만큼을 카운트
        cnt += cnt_coin
        # 해당 돈으로 내고 남은 돈 계산
        result %= coin

    return cnt

# 잔돈으로 받을 수 있는 돈의 종류 리스트
money = [500,100,50,10,5,1]
# 내가 내는 돈
n = int(input())
# 내가 내는 돈으로 받게될 잔돈 액수
give = 1000 - n

print(changed(give))