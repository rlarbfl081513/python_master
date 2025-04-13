# 힙이 제공하는 함수
1. 종류
   - heapq.heappush(heap, item)
     - 힙 불변성을 유지하면서 item값을 heap으로 푸쉬
   - heap.heappop(heap)
     - 힙 불변성을 유지하면서, 힙에서 가장 작은 항목을 팝하고 반환
   - heapq.heappushpop(heap, item)
     - 힙에서 item을 푸쉬, 힙에서 가장 작은 항목을 팝하고 반환, 
     - 힙푸쉬 후 힙팝을 별도로 호출하는 것보다 더 효율적
   - heap.heapify(x)
     - 리스트를 x선형 시간으로 제자리에서 힙으로 변환합니다.
   - heapq.heapreplace(heap, item)
     - 힙에서 가장 작은 항목을 팝하고 반환, 새로운 item도 푸쉬, 힙크기는 변경되지 않음
     - 힙 팝푸쉬하는것보다 효율적
     - 반환된 값은 추가한 item보다 클 수 있다. heappushpop을 하면 두 값 중 작은 값을 반환하여 힙에 큰값을 남긴다.
   - heapq.merge(*iterables, key=None, reverse=False)


---

## ✅ `heapq.heapreplace(heap, item)`

### 📌 개요

- **힙에서 가장 작은 항목을 제거하고(`pop`) 새로운 항목을 추가(`push`)**한다.
- 단일 연산으로 처리되므로, `heappop()` + `heappush()`보다 **더 효율적**이다.

### 📌 특징

- 힙의 **크기는 변하지 않는다**.
- 반환된 값은 새로 추가한 값보다 **클 수도 있다**.
- 내부에서 먼저 루트를 제거하고 새 항목을 루트에 넣은 후 `heapify-down` 실행

### 📌 사용 예시

```python
import heapq

heap = [1, 3, 5, 7, 9]
heapq.heapify(heap)
result = heapq.heapreplace(heap, 4)
print(result)  # 출력: 1 (기존 최소값)
print(heap)    # 출력: [3, 4, 5, 7, 9]
```

---

## ✅ `heapq.heappushpop(heap, item)`

### 📌 개요

- **힙에 item을 푸쉬(push)**한 뒤, **가장 작은 값을 팝(pop)해서 반환**한다.
- `heappush()` 후 `heappop()`을 별도로 호출하는 것보다 **더 효율적**이다.

### 📌 특징

- push와 pop이 동시에 일어나므로, 힙의 크기는 **변하지 않는다**.
- 삽입하려는 item이 기존 루트보다 **크면**, 루트가 제거되고 item이 남음
- 반대로 item이 **작으면**, item이 바로 반환됨 (힙에는 기존 값 그대로 유지됨)
  - 왜냐면 넣는다고 해도 어차피 힙구조는 그대로일거고 아무일도 안일어날거기에 굳이 싶은거니까 최적화를 위해서 변화가 일어나지 않을 수는 애초에 넣지도 안는 거임

### 📌 사용 예시

```python
import heapq

heap = [3, 5, 7, 9]
heapq.heapify(heap)
result = heapq.heappushpop(heap, 2)
print(result)  # 출력: 2 (item이 가장 작아서 pop됨)
print(heap)    # 출력: [3, 5, 7, 9] (기존 값 유지)
```

---

## ✅ 비교: `heappushpop()` vs `heapreplace()`

| 함수                        | 작동 순서                                   | 반환 값           | 남는 값            |
| ------------------------- | --------------------------------------- | -------------- | --------------- |
| `heappushpop(heap, item)` | 먼저 **item을 push** → 그 후 가장 작은 값 pop     | 두 값 중 **작은 값** | **큰 값이 힙에 남음**  |
| `heapreplace(heap, item)` | 먼저 **가장 작은 값 pop** → 그 후 **item을 push** | 기존 **최소값**     | **item이 힙에 남음** |

---

## ✅ `heapq.merge(*iterables, key=None, reverse=False)`

### 📌 개요

- 여러 **정렬된(iterable) 시퀀스를 병합**하여 **정렬된 iterator**를 반환한다.
- 내부적으로 **heap 기반 정렬 병합**을 수행하므로 **효율적**이다.

### 📌 특징

- 입력 시퀀스들은 **정렬되어 있어야 한다** (정렬 안 된 경우 정렬된 결과 보장 안 됨)
- 반환 값은 **iterator** (리스트가 아님 → 필요시 `list()`로 감싸기)
- `key`와 `reverse` 옵션도 제공 (Python `sorted()`와 유사)

### 📌 사용 예시

```python
import heapq

a = [1, 4, 7]
b = [2, 5, 8]
c = [0, 3, 6]

merged = heapq.merge(a, b, c)
print(list(merged))  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

### 📌 유용한 활용처

- 다중 정렬 결과의 **실시간 병합**
- 대용량 로그 파일 정렬 결과를 합칠 때 등
- 정렬된 큐/스트림 처리에 적합

---

## ✅ 요약 비교

| 함수              | 용도                   | 반환 값           | 특징             |
| --------------- | -------------------- | -------------- | -------------- |
| `heapreplace()` | 힙에서 pop + push 단일 연산 | 기존 루트 값        | 효율적이고 힙 크기 유지  |
| `heappushpop()` | push + pop 단일 연산       | 두 값 중 작은 값     | 삽입과 제거를 동시에 수행 |
| `merge()`       | 정렬된 iterable 병합      | iterator (정렬됨) | 입력은 정렬되어 있어야 함 |

---

셋 다 효율성과 성능이 중요한 상황에서 유용하게 활용될 수 있는 고급 함수이다.

