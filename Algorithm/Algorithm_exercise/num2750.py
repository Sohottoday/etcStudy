# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 1. 선택 정렬 알고리즘으로 문제 해결하기
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i       # 가장 작은 원소의 인덱스
    
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]         # 스왑, 위치 변경

for i in array:
    print(i)


# 2. 파이썬의 기본 정렬 라이브러리로 문제 해결하기

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)