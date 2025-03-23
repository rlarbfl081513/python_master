# ✅ 재귀 함수에서 return 정리

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
## 재귀 중간에 전체함수 종료는 불가능
-  return 값 전달 또는 global flag 방식으로 빠른 탈출은 가능
- 재귀는 내부적으로 스택에 쌓이기에, 한 재귀가 리턴되어도 그걸 호출한 함수로 돌아가야한 그 다음 함수가 종료됨

---
### 해당 코드
[swea : 미로 길찾기 문제](./BFS_&_DFS_&_RECURSION/SWEA/21684_miro.py)

> `return`은 한 함수만 종료시킴. 재귀에서는 계속 전달해줘야 의미 있음!

---
# ✅ DFS 경로 추적은 백트래킹으로 하기

- DFS는 한 방향으로 끝까지 가기 때문에, 경로 추적이 용이하다.
- 경로를 리스트에 저장할 때는 path.append() 후, 재귀가 끝나면 반드시 path.pop() 해줘야 한다.
- 그렇지 않으면 막다른 길을 포함한 잘못된 경로가 함께 출력된다.

## 백트래킹이 뭐죠
- 가보자 -> 아 안되네 -> 돌아가자 -> 다른 길로 가보자
- 어떤 조건을 만족하지 않으면 그 자리에서 중단하고 이전 단계로 돌아가는 알고리즘 기법 (되돌아가기 + 다음 시도)

### 해당 코드
[swea : 미로 길찾기 문제](./BFS_&_DFS_&_RECURSION/SWEA/21684_miro.py)

### 백트래킹이 사용된 부분
```python
path.append((ny, nx))          # 현재 경로 추가
found = recursion_miro(ny, nx) # 다음 위치 탐색
if found:
return True                # 도착했으면 종료
path.pop()                     # ❗ 이게 백트래킹: 실패한 경로 제거

# 경로에 ny,nx를 넣고 재귀호출
# 만약 도착못하면 그 경로는 실패한 길이니까 pop()해서 되돌림(그 경로는 버임)
# 그기로 다른 방향 탐색하면서 다시 어팬드
```
### 이 코드가 백트래킹 구조라고 할 수 있는 이유
- dfs기반으로 하나의 경로를 따라 이동, 깊이 탐색
- 도착못하면 pop으로 되돌아가고 다른 방향 탐색
- 도착하면 return True로 경로 유지
- path.append() / path.pop() / return True 각각이 백트래킹의 퍼즐 조각

# ✅ 재귀 함수에서 return 사용 기준 정리

## 핵심 질문
> 재귀 함수 끝에 `return`을 붙여야 할까? 붙이지 않아도 될까?

## 기준 요약
| 상황 | `return` 필요 여부 | 설명 |
|------|------------------|------|
| 재귀 호출의 **결과를 전달**하거나 누적할 때 | ✅ 필요 | 상위 함수에서 결과를 받아야 할 때 (예: 계산, 탐색 등) |
| 단순히 **로직을 이어가기 위한 호출**일 때 | ❌ 생략 가능 | 출력, 상태 변경 등 결과를 사용할 필요 없을 때 |

---

## return이 꼭 필요한 경우

### 1. 누적 계산 (예: 팩토리얼, 피보나치)
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### 2. 결과를 위로 전달 (예: DFS 탐색 결과)
```python
def find(node):
    if node == target:
        return True
    for child in node.children:
        if find(child):
            return True
    return False
```

---

## return 없이 호출만 해도 되는 경우

### 1. 출력만 하는 재귀
```python
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)  # return 없어도 무방
```

### 2. 상태만 바꾸는 재귀
```python
def fill(grid, y, x):
    if grid[y][x] == 1:
        return
    grid[y][x] = 1
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        fill(grid, y+dy, x+dx)  # return 불필요
```

---

## 결론
- 결과값을 전달하거나 사용할 목적이면 `return`을 꼭 붙인다
- 호출만 필요할 경우에는 `return`을 생략해도 실행 흐름에는 영향 없음

> 리턴값을 **다시 쓸 필요가 있는가?** → 이게 return 여부를 결정하는 기준이다.

