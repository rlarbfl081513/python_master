
# 🔍 리스트 탐색 vs 집합 탐색 성능 비교

## ✅ 문제 상황
- 2차원 배열(아파트 주민)을 순회하며, 특정 값(블랙리스트)이 포함되어 있는지 확인해야 하는 경우
- 다음과 같이 `if val in 리스트:`를 반복 수행하면 **시간 초과** 가능성이 높음

## 🐢 리스트(List) 탐색
```python
if val in some_list:
    ...
```

- **시간복잡도**: O(N)
- 리스트는 처음부터 끝까지 순차적으로 비교함
- 데이터 수가 많아질수록 선형 시간 증가

## ⚡ 집합(Set) 탐색
```python
some_set = set(some_list)
if val in some_set:
    ...
```

- **시간복잡도**: 평균 O(1)
- `HashTable` 기반으로 구현되어 있어 탐색이 빠름
- **조건 판단이 많은 경우 필수적으로 사용해야 시간초과 방지 가능**

---

## 🔧 적용 예시

### 문제 코드 (시간 초과 발생 가능)
```python
for row in a_arr:
    for val in row:
        if val in blacklist_list:  # O(N) 연산 반복
            cnt += 1
```

### 개선 코드 (set으로 변경)
```python
blacklist_set = set(sum(b_arr, []))  # 2차원 리스트를 1차원으로 평탄화 후 집합 변환

for row in a_arr:
    for val in row:
        if val in blacklist_set:  # O(1) 연산으로 개선
            cnt += 1
```

---

## ⛳ 실전 팁

| 상황 | 리스트(List) | 집합(Set) |
|------|------------------|--------------------|
| 순서를 유지해야 함 | ✅ 사용 가능 | ❌ 순서 없음 |
| 중복 제거가 필요함 | ❌ 불리함 | ✅ 자동 제거 |
| 탐색 성능이 중요함 | ❌ 느림 (O(N)) | ✅ 빠름 (O(1)) |
| 데이터 크기가 크고 `in` 연산이 많음 | ❌ 시간초과 위험 | ✅ 최적 |

---

## 📌 결론
> `if val in 리스트:`를 반복적으로 사용할 경우, 리스트 대신 **집합(set)** 으로 변환해서 사용하면 시간 복잡도를 **O(N) → O(1)** 로 줄일 수 있다.

---

# 🔢 dat 리스트란 무엇인가?

## ✅ 정의
`dat`는 일반적으로 알고리즘 문제나 대회 코드에서 자주 사용되는 **"데이터 체크 배열"**을 의미하는 변수명으로, **특정 정수 값의 존재 여부나 상태를 빠르게 확인하기 위해 사용하는 리스트**입니다.


## ✅ 왜 `dat`라는 이름을 사용할까?

| 관습적 약어 | 의미 |
|-------------|------|
| `dat`       | `data` 또는 `data table`의 축약형으로, 데이터의 상태를 저장하는 공간이라는 의미로 자주 사용됨 |

- 프로그래밍 대회나 알고리즘 문제에서는 **간결한 변수명을 선호**하기 때문에 `check_list`, `exist_table`보다 `dat`가 짧고 빠르게 쓸 수 있음
- C언어나 Python에서 빠른 인덱스 접근이 가능한 구조로, **`dat[num]`이라는 형태로 빠른 조회**가 가능하게 하려는 목적

---

## ✅ 사용하는 이유: 고속 탐색

- 일반적으로 어떤 값이 **존재하는지 확인**할 때 `list`의 `in` 연산자나 `set`, `dict`를 사용하는데,
  ```python
  if num in my_set:  # O(1) 평균 시간
  ```
- 하지만 **숫자의 범위가 고정되어 있고 작을 경우**, 리스트의 인덱스를 직접 활용하면 더 빠르게 확인할 수 있음
  ```python
  dat = [0] * 100001
  dat[37] = 1  # 존재 표시
  if dat[37]:  # 빠른 확인
      print("존재함")
  ```

---

## ✅ 예시 코드: 블랙리스트 확인
```python
T = int(input())

for tc in range(1, T + 1):
    h, w = map(int, input().split())
    apartments = [list(map(int, input().split())) for _ in range(h)]

    bh, bw = map(int, input().split())
    black_list = [list(map(int, input().split())) for _ in range(bh)]

    dat = [0] * 100001  # 최대 값이 100000이라고 가정

    # 블랙리스트 체크
    for i in range(bh):
        for j in range(bw):
            dat[black_list[i][j]] = 1

    black_cnt = 0
    for i in range(h):
        for j in range(w):
            if dat[apartments[i][j]]:
                black_cnt += 1

    print(f'#{tc} {black_cnt} {(h*w) - black_cnt}')
```

---
## ✅ 예시 코드: 성실한 사원
- dat의 런타임에러시, 범위를 너무 크게 잡은거니까 
- 인풋에 따라 dat 리스트의 길이를 조정할 수 있도록 한다.
- [swea : 성실한 사원](../algorithm/List_&_String/List/21463_DAT-good-staft.py)
---

## ✅ 정리
| 항목 | 설명 |
|------|------|
| 목적 | 정수형 데이터의 존재 여부를 빠르게 확인하기 위함 |
| 이름 | `dat`는 관습적으로 쓰이는 약어 (`data table` 느낌) |
| 특징 | 고정된 정수 범위에서 매우 빠른 탐색 (O(1)) |
| 주의 | 정수 값의 범위가 크면 메모리 낭비 가능 |

---