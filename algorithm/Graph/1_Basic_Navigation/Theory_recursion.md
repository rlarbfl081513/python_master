# 재귀 함수에서 return 정리

## 핵심 요약
- 재귀 함수를 사용할 때 `return`이 함수 전체를 종료하지 않고, "현재 함수 호출 한 번만 종료"된다는 점을 이해해야 한다.
- `return`은 **현재 함수 호출 한 번만 종료**한다.
- 재귀에서는 원하는 값을 **계속 return으로 전달**해야 최종 출력까지 도달할 수 있다.
- 또는 `global` 변수로 결과를 저장해 함수 외부에서 출력할 수도 있다.

---

## 두 가지 방식 비교

### 1. return 전파 방식
```python
def dfs(y, x):
    if arr[y][x] == 3:
        return 1
    visit[y][x] = True

    for dy, dx in [(-1,0),(0,1),(1,0),(0,-1)]:
        ny, nx = y + dy, x + dx
        if 조건:
            result = dfs(ny, nx)
            if result == 1:
                return 1
    return 0

# 함수 흐름 구조
# recursion_miro(시작)
#  └ recursion_miro(다음)
#     └ recursion_miro(다음)
#        └ 도착! → return 1
#     ← result == 1 → return 1
#  ← result == 1 → return 1
# → 최종 print(1)

```
- 최종 출력: `print(dfs(y, x))`

### 2. global 변수 방식
```python
res = 0

def dfs(y, x):
    global res
    if arr[y][x] == 3:
        res = 1
        return
    visit[y][x] = True

    for dy, dx in [(-1,0),(0,1),(1,0),(0,-1)]:
        ny, nx = y + dy, x + dx
        if 조건:
            dfs(ny, nx)
```
- 최종 출력: `print(res)`

---

## 상황에 따라 선택
- 간단한 문제 → `global 변수 방식`
- 함수형 구조/반환값 필요 → `return 전파 방식`

---
### 해당 코드
[swea : 미로 길찾기 문제](./BFS_&_DFS_&_RECURSION/SWEA/21684_miro.py)

> `return`은 한 함수만 종료시킴. 재귀에서는 계속 전달해줘야 의미 있음!

