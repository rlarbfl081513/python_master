
# 동전의 종류는 n개 --> 합을 k로 만든다 --> 최소한의 동전개수로

def coin(total):
    cnt = 0
    for i in arr:
        cnt_pre = total // i
        cnt += cnt_pre
        total %= i

    return cnt


n,k = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
# 큰수의 동전부터 넣도록 리스트를 뒤집어서 내림차순을 한다
arr.reverse()
print(coin(k))