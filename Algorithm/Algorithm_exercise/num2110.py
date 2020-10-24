# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
#  최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
#  가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
#  둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (1 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# 예제 입력 1 
# 5 3
# 1
# 2
# 8
# 4
# 9
# 예제 출력 1 
# 3

# 문제 유형 : 이진 탐색

# 문제 풀이 핵심 아이디어
## 집의 개수 N은 최대 200,000이며, 집의 좌표 X는 최대 1,000,000,000 이다.
## 이진 탐색을 이용하여 O(N * logX)에 문제를 해결할 수 있다.
## 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾는다.

## 반복적으로 Gap을 설정하며, C개 이상의 공유기를 설치할 수 있는 경우를 찾는다.(N=5, C=3)
## 최대 Gap = 8
## 최소 Gap = 1    (8 + 1)/2 = 4         Gap = 4
## 공유기 : 2개

## 최대 Gap = 3
## 최소 Gap = 1    (3 + 1)/2 = 2         Gap = 2
## 공유기 : 3개
## 설치 가능한 공유기의 개수가 C 이상이므로 현재의 Gap을 저장한 뒤에 Gap을 증가시킨다.

## 최대 Gap = 3
## 최소 Gap = 3     Gap = 3
## 공유기 : 3개
## 더이상 Gap을 증가시킬 수 없으므로, 최적의 경우

n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2        # mid는 Gap을 의미한다.
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    
    if count >= c:      # c개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid    
    else:               # c개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1

print(result)


# 이진 탐색 문제는 난이도가 낮은 문제가 없다.