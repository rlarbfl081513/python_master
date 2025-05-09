## ✅ 이터러블(iterable) vs 이터레이터(iterator)

### 🔹 이터러블 (iterable)

* 반복 가능한 객체
* 내부에 `__iter__()` 메서드를 가지고 있음
* `for`문으로 돌릴 수 있음
* 하지만 `next()`로 바로 꺼낼 수는 없음 (iter로 변환 필요)

**예시:** `list`, `tuple`, `str`, `range`, `dict`

```python
lst = [1, 2, 3]
for i in lst:
    print(i)  # OK

next(lst)  # ❌ 에러: 리스트는 이터러블이지만 이터레이터는 아님
```

---

### 🔹 이터레이터 (iterator)

* 값을 하나씩 꺼낼 수 있는 객체
* `__iter__()`와 `__next__()` 메서드를 모두 가지고 있음
* `next()` 함수로 직접 값을 꺼낼 수 있음

이터러블을 `iter()` 함수로 감싸면 이터레이터가 됨:

```python
lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # ❌ StopIteration 에러
```

---

## ✅ 둘의 관계 요약

| 구분           | iterable               | iterator                       |
| ------------ | ---------------------- | ------------------------------ |
| 반복 가능        | ✅                      | ✅                              |
| `__iter__()` | ✅                      | ✅                              |
| `__next__()` | ❌                      | ✅                              |
| `next()` 사용  | ❌                      | ✅                              |
| 예시           | `list`, `str`, `range` | `iter(list)`, `map()`, `zip()` |

---

## ✅ 파이썬에서 자주 쓰는 이터레이터들

* `iter(리스트/문자열)` → 이터레이터로 변환
* `map(func, iterable)`
* `filter(func, iterable)`
* `zip(iter1, iter2)`

이런 것들은 직접 출력하면 `<map object>`, `<zip object>`처럼 나옴 → **지연 평가(lazy evaluation)** 때문

```python
s = 'hello'
it = iter(s)
print(next(it))  # 'h'
```

---

## ✅ 왜 이터레이터가 중요할까?

* 메모리 아끼기: 전체 리스트 안 만들고, **하나씩 계산하며 꺼냄**
* 속도 향상: 필요할 때만 평가하는 **지연 평가(lazy evaluation)**
* 파일 읽기, 무한 스트림, 대용량 데이터 처리 등에 핵심적

