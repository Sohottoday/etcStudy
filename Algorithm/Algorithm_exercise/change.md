# 방향 전환

- 대표적인 문제 BFS/DFS
- 2/3 차원


### 가장 기본적인 방법
if way == 'N':
    x += -1
    y += 0
elif way == 'S':
    x += 1
    y += 0
elif way == 'E':
    x += 0
    y += 1
else:
    x += 0
    y += -1

위 식을 표로 정리하면
    N   S   E   W
x   -1  1   0   0
y   0   0   1   -1

이걸 파이썬 코드로 변환하면
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

이걸 약간 변형시킬 때 시계방향 혹은 반시계방향으로 꺾으라는 의미의 문제가 나온다면
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]      반시계 방향

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]      시계 방향

이러한 것을 응용하면
if way == 'N':
    x -= 1
elif way == 'S':
    x += 1
elif way == 'E':
    y += 1
else:
    y -= 1

이러한 코드를
x += dx['ENSW'.index(way)]
y += dy['ENSW'.index(way)]
이렇게 줄일 수 있다.

for i in range(4):
    dfs(x + dx[i], y + dy[i])
이렇게 dfs 를 풀이할 수 있다.
