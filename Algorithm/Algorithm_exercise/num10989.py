# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1 
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7

# 문제 풀이 핵심 아이디어
# 1. 데이터 개수가 최대 10,000,000개
# 2. 시간 복잡도 O(N)의 정렬 알고리즘을 이용해야 한다.
# 3. 수의 범위가 1~10000 이므로 계수 정렬을 이용할 수 있다.

# 계수 정렬(Counting Sort) 알고리즘
## 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
## 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정한다.
## 데이터가 등장한 횟수를 센다.

## 유의사항 : 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()를 사용해야 한다. -> 기본적인 input() 함수보다 빠르다.

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)