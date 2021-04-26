
# 예외 처리

## 조건문과 반복문

### 1. 논리 연산자 / 비트 연산자 활용하기
if a > b:
    if a % 10 == 0:
        print(a)

위와 같은 코드를 작성할 경우 짧게 진행할 수 있도록 활용한다.

if a > b and a % 10 == 0:
    print(a)

- and or not 등등

1 << 2, 1 & 1, 1 | 1, 1 ^ 1 등 비트 연산자도 잘 활용하면 좋다.

### 2. 상태를 나타내는 자료 활용하기
N = 71
ck = False
for i in range(1, N):
    if N % i == 0:
        print("Not Prime")
        ck = True
        break

if not ck:
    print("Prime")

### 3. 나눠서 진행하기
def isPrime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

for N in range(10, 100):
    if isPrime(N):
        print(f"{N} if Prime")
    else:
        print("Not Prime")

### 4. 여러 자료구조와 메서드, 함수 활용하기
S = "hello"

for idx in S:
    if S[idx] != S[len(S) - idx - 1]:
        print("Not Palin")

위를 줄이면
if S == S[: : -1]:
    print("isPalin")

리스트의 특성을 활용한다.

def isUnique(lst):
    return len(lst) == len(set(lst))
위와 같은 방식으로 중복을 확인할 수 있다.

### 5. 미리 처리한 케이스와 처리할 케이스 정리하기
1. 예제 케이스
2. 조건 a 처리
3. 조건 b 처리
4. 조건 ab 처리

### 6. 예제, 최소, 최대, 예외, 랜덤 케이스 만들기
1. 예제
