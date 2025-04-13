# 인풋의 정수 처리 방식 
   1. 질문 : 23 03434 이거를 n,num = map(int, input().split())이렇게 받아오는데 왜 0이 빠져서 받아지지? 
   2. 대답 : input()은 문자열로 받아오고, map(int, input().split())은 그걸 **정수(int)**로 바꾸기 때문에 숫자 앞의 0은 자동으로 사라져.

         ```python
          n, num = map(int, input().split())
          # 입력: 23 03434
          # 결과: n = 23, num = 3434   ← 앞의 0이 사라짐!
         ```
         ```python
            ## 출력 테스트_1
            n,m = map(int,input().split())
            
            print(f'출력 : {n} 과 {m}')
            
            # 입력 0 00
            # 출력 0 0
            #
            # 입력 0 0
            # 출력 0 0
            #
            # 입력 10 01
            # 출력 10 1
            
            
            ## 출력 테스트_2
            num_arr = [list(map(int,input().split())) for _ in range(2)]
            
            for row in num_arr:
                print(row)
            
            # 입력
            # 0 0 0 0
            # 10 01 001 0001
            # 출력
            # [0, 0, 0, 0]
            # [10, 1, 1, 1]
            
            
            ## 출력 테스트_3
            str_arr = [list(input().split()) for _ in range(2)]
            
            for row in str_arr:
                print(row)
            
            # 입력
            # 0 0 0 0
            # 10 01 001 0001
            # 출력
            # ['0', '0', '0', '0']
            # ['10', '01', '001', '0001']
            
            for row in str_arr:
                for i in row:
                    print(int(i), end=" ")
                print()
            
            # 입력
            # 0 0 0 0
            # 10 01 001 0001
            # 출력
            # 0 0 0 0
            # 10 1 1 1
            
            # 0으로 시작되는 숫자는 문자열로 받으면 가능
            for_str_print = ['0','01','001']  # ['0', '01', '001']
            
            # 0으로 시작하는 숫자를 정수로 썻을때 에러 발생
            # 파이선에서 0으로 시작하는 숫자는 예전에 8진수로 인식됐는데, 파이선3부터는 혼란방지를 위해 막음
            # for_num_print = [0, 01, 001]  # 에러 발생
            
            # 8진수로 쓰고 싶다면 0o를 붙여
            for_num_print = [0o0, 0o01, 0o001]  # [0, 1, 1]
            
            print(for_num_print)

         ```
#
# `sys.stdin.readline()` 이색기 끝에 엔터 들어가 자동으로?

네, `sys.stdin.readline()`은 입력을 받을 때 **문자열 끝에 개행 문자 (`\n`)** 가 자동으로 포함됩니다.

그래서 `input()`을 호출하면 기본적으로 **입력값 + `\n`** 형태가 됩니다.

**예제 확인**

```python
import sys
input = sys.stdin.readline

data = input()
print(f"입력값: {data}")  # 개행 문자 포함 확인
print(f"입력값 길이: {len(data)}")
```

**입력**

```
Hello
```

**출력**

```
입력값: Hello
 (개행 문자 포함됨)
입력값 길이: 6
```

- **"Hello"는 5글자인데, 길이가 6인 이유?**
- 문자열 끝에 `\n`이 자동으로 포함되었기 때문!

**정리**

`sys.stdin.readline()` 사용 시 **자동으로 `\n` 포함됨**

필요하면 `rstrip()`으로 제거 가능 (`strip()` 사용 시 공백까지 제거되므로 주의)

백준 같은 곳에서는 개행 문자 때문에 **출력 형식 오류**가 발생할 수 있으니 조심! 🚀

## 파일에서 입력받을 때도 개행문자 포함 가능

`sys.stdin = open('input.txt')` 로 **파일에서 입력을 받을 때도 개행 문자(`\n`)가 포함될 수 있습니다.**

즉, 파일의 마지막 줄을 제외하고는 **각 줄 끝에 `\n`이 포함된 상태**로 `input()`이 읽어옵니다.

---

### **파일 입력에서 개행 문자 포함 여부 확인**

**예제 (`input.txt` 내용)**

```
Hello
World
```

### **코드**

```python
import sys
from collections import deque

sys.stdin = open('input.txt')  # 파일 입력
input = sys.stdin.readline  # 한 줄씩 읽음

word1 = deque(input())  # 첫 번째 줄 읽기
word2 = deque(input())  # 두 번째 줄 읽기

print(f"word1: {list(word1)}")  # deque 내부 확인
print(f"word2: {list(word2)}")
```

### **출력**

```
word1: ['H', 'e', 'l', 'l', 'o', '\n']
word2: ['W', 'o', 'r', 'l', 'd']
```

**개행 문자(`\n`)가 포함된 것을 확인 가능!**

즉, `sys.stdin = open('input.txt')`를 사용하더라도 개행이 포함될 수 있습니다.

## 직접 콘솔 입력 시 개행 포함됨

만약 **`sys.stdin = open('input.txt')` 없이 직접 콘솔에서 입력**하고 `hello`를 입력한 뒤 **엔터(Enter)** 를 치면, `sys.stdin.readline()`을 사용할 때 **자동으로 개행(`\n`)이 포함됩니다.**

---

### **예제 코드**

```python
import sys
from collections import deque

input = sys.stdin.readline  # 표준 입력 사용

word = deque(input())  # 한 줄 입력 받기
print(f"리스트 형태: {list(word)}")  # deque 내부 확인
print(f"마지막 문자: {word[-1]!r}")  # 개행 문자가 포함되었는지 확인
```

---

### **입력 (콘솔에서 직접 입력)**

```
hello (Enter 입력)
```

### **출력 결과**

```
리스트 형태: ['h', 'e', 'l', 'l', 'o', '\n']
마지막 문자: '\n'
```

- **마지막 문자로 개행(`\n`)이 포함된 것을 확인할 수 있음.**

---

## **왜 개행이 포함될까?**

`sys.stdin.readline()`은 **Enter 키를 입력할 때 개행(`\n`)까지 포함해서 읽어오기 때문**입니다.

이와 다르게 `input()`은 자동으로 개행을 제거하여 반환합니다.

### **비교**

| 입력 방식 | 개행 포함 여부 |
| --- | --- |
| `input()` | ❌ 개행 포함되지 않음 |
| `sys.stdin.readline()` | ✅ 개행 포함됨 |

## **개행 문자 제거 방법**

### 방법 1: `rstrip()` 사용

```python
data = input().rstrip()  # 개행 문자 제거
print(f"입력값: {data}")
print(f"입력값 길이: {len(data)}")

# 출력
입력값: Hello
입력값 길이: 5
```

### 방법 2: `pop()` 사용 (마지막이 개행 문자일 경우만 제거)

```python
word = deque(input())
if word[-1] == '\n':  # 개행 문자가 마지막에 있으면 제거
    word.pop()
```

### 방법 3: 파일 읽을 때 개행문자 제거

```python
with open("input.txt", "r") as f:
    for line in f:
        print(repr(line.rstrip()))  # 개행 문자 제거
```

```
'Hello'
'World'
'Python'
```

**파일을 다룰 때 `rstrip()`을 사용하면 개행 문제를 자동으로 해결 가능!** 

---

위 예제에서  **`with open("input.txt", "r") as f:`의 의미**

이 구문은 **파일을 열고(`open()`) 자동으로 닫아주는(`with`) Python의 파일 처리 방식**입니다.

## **1. `with` 문이 필요한 이유**

파일을 다룰 때 **파일을 열고(`open`) 닫는(`close`) 것이 중요**합니다.

`with` 문을 사용하면 **자동으로 파일을 닫아주기 때문에** `close()`를 직접 호출할 필요가 없어요.

### **비효율적인 코드 (직접 `close()` 호출)**

```python
f = open("input.txt", "r")  # 파일 열기
data = f.read()  # 파일 내용 읽기
print(data)
f.close()  # 파일 닫기 (반드시 필요!)
```

`close()`를 호출하지 않으면 **파일이 계속 열린 상태로 남아 메모리 낭비가 발생**할 수 있음.

---

### **`with` 문을 사용한 효율적인 코드**

```python
with open("input.txt", "r") as f:
    data = f.read()  # 파일 내용 읽기
    print(data)  # 파일 자동으로 닫힘
```

**`with`를 사용하면 블록(`with` 내부 코드)이 끝나면 파일이 자동으로 닫힘!**

**파일을 열다가 에러가 나도 안전하게 닫힘** (메모리 누수 방지).

---

## **2. `open("input.txt", "r")`의 의미**

```python
open("파일명", "모드")
```

- `"input.txt"` → **읽거나 쓸 파일의 이름**
- `"r"` → **읽기(`read`) 모드로 파일 열기**

| 모드 | 설명 |
| --- | --- |
| `"r"` | 읽기 모드 (파일이 있어야 함) |
| `"w"` | 쓰기 모드 (파일이 없으면 생성, 기존 내용 삭제됨) |
| `"a"` | 추가 모드 (기존 파일에 내용 추가) |
| `"rb"`, `"wb"` | 바이너리(`binary`) 모드 |

---

## **3. `as f`는 무엇을 의미할까?**

```python
with open("input.txt", "r") as f:
```

📌 여기서 `as f`는 **파일 객체를 `f`라는 변수에 저장**하는 역할을 합니다.

이제 `f`를 사용해서 파일을 읽거나 쓸 수 있어요.

### **예제: 파일 한 줄씩 읽기**

```python
with open("input.txt", "r") as f:
    for line in f:  # 파일을 한 줄씩 읽음
        print(line.rstrip())  # 개행 문자 제거 후 출력
```

---

## **4. `with` 문이 자동으로 `close()`를 호출하는 원리**

```python
with open("input.txt", "r") as f:
    data = f.read()

# 여기서 파일이 자동으로 닫힘!
```

**Python의 `with` 문은 `__enter__()`와 `__exit__()` 메서드를 사용**

`open()`을 실행하면 `__enter__()`가 파일을 열고, `with` 블록이 끝나면 `__exit__()`가 `close()`를 자동으로 호출!

---

## **정리**

| 구문 | 설명 |
| --- | --- |
| `open("input.txt", "r")` | `input.txt` 파일을 읽기(`r`) 모드로 염 |
| `with open("input.txt", "r") as f:` | `f`를 통해 파일을 다루며, 자동으로 닫음 |
| `f.read()` | 파일 전체를 읽음 |
| `f.readline()` | 한 줄씩 읽음 |
| `f.readlines()` | 모든 줄을 리스트로 반환 |

✔ **`with open()`을 사용하면 `close()`를 호출할 필요 없이 안전하게 파일을 닫아줌!** 🚀

# **`rstrip()`이란?**

`rstrip()`은 **문자열 끝(`오른쪽`)의 불필요한 공백이나 특정 문자를 제거하는 함수**예요.

---

## **1. 기본 사용법 (오른쪽 공백 제거)**

```python
text = "Hello World   "  # 오른쪽에 공백이 있음
print(repr(text.rstrip()))  # 공백 제거 후 출력

# 출력: 'Hello World'  (오른쪽 공백이 사라짐)
```

`rstrip()`을 사용하면 **문자열 끝의 공백이 제거됨**.

---

## **2. 특정 문자 제거**

`rstrip("제거할 문자")`를 사용하면 **특정 문자만 제거**할 수도 있어요.

```python
text = "Hellooo!!!???"
print(text.rstrip("!?"))  # '!'와 '?'를 제거
# 출력 Hellooo

text = "Hellooo!!!abc?!??"
print(text.rstrip("!?"))  # '!'와 '?'를 제거
# 출력 Hellooo!!!abc

text = "Hellooo!!!abc???"
print(text.rstrip("!?abc"))  # '!'와 '?'를 제거
# 출력 Hellooo
```

- **오른쪽(`right`)에서만 "o"가 제거됨**
- **중간에 있는 문자는 제거되지 않음!**

---

## **3. 개행 문자 `\n` 제거 (파일 읽기 시 유용)**

파일을 읽을 때 줄바꿈 문자 `\n`이 포함될 수 있는데, 이를 제거할 때 `rstrip()`을 사용하면 좋아요.

```python
text = "Hello\n"
print(repr(text))  # 개행 문자 포함된 상태
print(repr(text.rstrip()))  # 개행 문자 제거

# 출력:
# 'Hello\n'  (개행 문자가 있음)
# 'Hello'    (개행 문자 제거됨)
```

- **파일을 읽을 때 `rstrip()`을 쓰면 `\n`이 자동으로 제거됨!**

---

## **4. 여러 개의 문자 제거 가능**

`rstrip("제거할 문자들")`을 사용하면 **여러 개의 특정 문자도 제거 가능**해요.

```python
text = "Hellooo!!!???"
print(text.rstrip("!?"))  # '!'와 '?'를 제거

# 출력: 'Hellooo'
```

- 오른쪽 끝에 있는 `!`와 `?`만 제거됨.
- **중간에 있는 문자는 영향을 받지 않음!**
- pop()처럼 오른쪽 끝에서 부터 확인하는 것으로, 만약 !?가 아닌 다른 문자가 나오면 멈춘다

---

## **5. `lstrip()`과 `strip()` 차이**

| 함수 | 역할 |
| --- | --- |
| `rstrip()` | **오른쪽**(끝) 공백/특정 문자 제거 |
| `lstrip()` | **왼쪽**(시작) 공백/특정 문자 제거 |
| `strip()` | **양쪽** 공백/특정 문자 제거 |

```python
text = "   Hello World   "

print(repr(text.lstrip()))  # 왼쪽 공백 제거
print(repr(text.rstrip()))  # 오른쪽 공백 제거
print(repr(text.strip()))   # 양쪽 공백 제거

# 출력:
# 'Hello World   '
# '   Hello World'
# 'Hello World'
```

---

## **정리**

- **`rstrip()` → 문자열 오른쪽 끝의 공백 또는 특정 문자 제거**
- **파일 읽을 때 `rstrip("\n")`을 사용하면 줄바꿈 문제 해결 가능**
- **왼쪽을 제거하려면 `lstrip()`, 양쪽을 제거하려면 `strip()` 사용**