# 문제 유형 : 백트래킹

# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 예제 입력 1 
# 8
# 예제 출력 1 
# 92

# 문제 풀이 핵심 아이디어
## DFS를 이용하여 간단히 백트래킹 알고리즘을 구현할 수 있다.
## DFS는 재귀를 활용하기 때문에 구현이 간단하지만 시간 조건이 부족하다면 BFS를 활용해도 된다.

# X번째 행에 놓은 Queen에 대해서 검증
def check(x):
    # 이전 행에 놓았던 모든 queen들을 확인
    for i in range(x):
        # 위쪽 혹은 대각선을 확인
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
        return True

# x번째 행에 대하여 처리
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # x 번째 행의 각 열에 queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            # 해당 위치에 queen을 두어도 괜찮은 경우
            if check(x):
                # 다음 행으로 넘어가기
                dfs(x+1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
