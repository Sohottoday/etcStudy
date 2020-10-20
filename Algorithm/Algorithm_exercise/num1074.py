# 문제
# 한수는 2차원 배열 (항상 2^N * 2^N 크기이다)을 Z모양으로 탐색하려고 한다. 
# 예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

# 만약, 2차원 배열의 크기가 2^N * 2^N라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 4등분 한 후에 (크기가 같은 2^(N-1)로) 재귀적으로 순서대로 방문한다.

# 다음 예는 2^2 * 2^2 크기의 배열을 방문한 순서이다.

# N이 주어졌을 때, (r, c)를 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 다음 그림은 N=3일 때의 예이다.

# 입력
# 첫째 줄에 N r c가 주어진다. N은 15보다 작거나 같은 자연수이고, r과 c는 0보다 크거나 같고, 2^N-1보다 작거나 같은 정수이다

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 1 
# 2 3 1
# 예제 출력 1 
# 11
# 예제 입력 2 
# 3 7 7
# 예제 출력 2 
# 63

def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return

    solve(n/2, x, y)
    solve(n/2, x, y+n/2)            # 4 X 4 배열에서 2X2 기준 2번째 배열이라는 의미
    solve(n/2, x+n/2, y)
    solve(n/2, x+n/2, y+n/2)

result = 0
N, X, Y = map(int, input().split(' '))      # X, Y는 좌표라 생각하면 된다. 
solve(2 ** N, 0, 0)                         # 0, 0은 시작점이 0, 0이라는 의미
