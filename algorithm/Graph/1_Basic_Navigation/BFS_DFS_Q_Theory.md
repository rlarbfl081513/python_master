# DFS / BFS 개념 정리

## DFS (Depth-First Search)

- 깊이 우선 탐색
- 한 방향으로 끝까지 들어갔다가 막히면 돌아와서 다른 길 탐색
- 재귀나 스택으로 구현
- visited 체크 필수

### 기본 코드 (재귀 방식)
```python
def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)
```

- 그래프 탐색, 경로 찾기, 백트래킹 문제에 자주 나옴


## BFS (Breadth-First Search)

- 너비 우선 탐색
- 시작점에서 가까운 것부터 탐색
- 큐 사용 (collections.deque)
- visited 체크 필수

### 기본 코드
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
```

- 최단 거리 구할 때 자주 사용


## 큐 관련 정리

- BFS는 무조건 큐 사용
- 일반 리스트로 하면 시간 초과 날 수 있어서 `deque` 써야 함

```python
from collections import deque

q = deque()
q.append(1)
q.popleft()
```


## DFS vs BFS 차이

| 항목 | DFS | BFS |
|------|-----|-----|
| 자료구조 | 스택 / 재귀 | 큐 |
| 탐색 순서 | 깊게 | 넓게 |
| 사용 예 | 경로 탐색, 백트래킹 | 최단거리, 레벨 탐색 |

