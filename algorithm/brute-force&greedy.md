# 완전탐색(Brute Force) vs 그리디(Greedy)

| 항목 | 완전탐색 (Brute Force) | 그리디 (Greedy) |
|------|------------------------|------------------|
| 핵심 아이디어 | 가능한 모든 경우를 시도 | 매 순간 최선의 선택을 함 |
| 전략 | 모든 조합/경우 탐색 | 현재 가장 좋아 보이는 선택 반복 |
| 시간복잡도 | 느림 (O(N!), O(2^N) 등) | 빠름 (보통 O(N log N), O(N)) |
| 결과 정확성 | 항상 정답을 보장함 | 항상 최적 해를 보장하지 않음 |
| 필요한 조건 | 없음 (작은 입력에 적합) | 탐욕적 선택 조건 + 최적 부분 구조 필요 |
| 예시 | 순열/조합, 백트래킹, 완전탐색 문제 | 동전 문제, 회의실 배정, 활동 선택 문제 |

---
## 예시 비교
- 동전 문제 (동전 개수 최소)
- 완전탐색: 모든 경우의 조합으로 거스름돈 만드는 경우 다 확인
- 그리디: 큰 동전부터 가능한 만큼 사용
    ```python
    [완전탐색]
  
    coins = [10, 50, 100]
    target = 130
    min_count = float('inf')
    
    def dfs(index, current_sum, count):
        global min_count
        if current_sum > target:
            return
        if current_sum == target:
            min_count = min(min_count, count)
            return
        for i in range(len(coins)):
            dfs(i, current_sum + coins[i], count + 1)
    
    dfs(0, 0, 0)
    print("완전탐색 결과:", min_count)  # 결과: 2 (100 + 30 → 50+50+30 안됨)
    ```
  ```python
  [그리디]
    
    coins = [100, 50, 10]
    target = 130
    count = 0
    
    for coin in coins:
        count += target // coin
        target %= coin
    
    print("그리디 결과:", count)  # 결과: 2 (100 + 30 → 30은 10x3)
  
    # 이 코드는 반복하지 않고, 수학적으로 계산해서 각 동전 몇 개 필요한지를 바로 구함
    # 그래서 target // coin으로 개수를 구하고,
    # target %= coin으로 남은 금액만 갱신하면 끝!
  
    # 그리디는 모든 경우에 정답을 보장하진 않아!
    # 예를 들어 동전이 [1, 3, 4]이고 금액이 6일 때,
    # 그리디는 4 + 1 + 1 = 3개 → 하지만 최적은 3 + 3 = 2개야.     
    ```
  


## 간단 요약
- 완전탐색은 답을 반드시 찾지만 느리고,
그리디는 빠르지만 항상 최적 해를 보장하진 않는다.
- 그리디는 “조건을 만족하는 문제”에만 쓰는 거고,
완전탐색은 “확실한 정답이 필요할 때” 쓰는 방법이야!