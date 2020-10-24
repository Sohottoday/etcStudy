# 문제
# N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

# 영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다.
#  물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다.
#  그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, M(1≤M≤100,000)이 주어진다. 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1≤A, B≤N), C(1≤C≤1,000,000,000)가 주어진다.
#  이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다. 서로 같은 두 도시 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다.
#  마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.

# 출력
# 첫째 줄에 답을 출력한다.

# 예제 입력 1 
# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3
# 예제 출력 1 
# 3

# 문제 유형 : 이진 탐색

# 문제 풀이 핵심 아이디어
## 다리의 개수 M은 최대 100,000이며, 중량 제한 C는 최대 1,000,000,000이다.
## 이진 탐색을 이용하여 O(M * logC)에 문제를 해결할 수 있다.
## 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 이진 탐색으로 찾는다.
## BFS를 활용한다.

## 반복적으로 중량을 설정하며, 이동이 가능한 경우를 찾는다(시작 노드 : 1, 도착 노드 : 3)
### 최대 중량 = 0, 최소 중량 = 2            결과 = 2(결과값을 최소값으로 초기화한 뒤) => 중량 = 5 =>(9 + 2)/2
    # 이동이 가능하므로 결과값 중량을 증가시킨다.
### 최대 중량 = 9, 최소 중량 = 6            결과 = 5 => 중량 = 7 => (9 + 6)/2
    # 이동이 불가능하므로, 중량을 감소시킨다.
### 최대 중량 = 6, 최소 중량 = 6            결과 = 5 => 중량 = 6
    # 이동이 불가능하므로, 중량을 감소시킨다. 더이상 감소시킬 수 없으므로 결과 = 5

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while(start <= end):
    mid = (start + end) // 2        # mid는 현재의 중량
    if bfs(mid):                    # 이동이 가능하므로, 중량을 증가시킨다.
        result = mid
        start = mid + 1
    else:                           # 이동이 불가능하므로, 중량을 감소시킨다.
        end = mid - 1

print(result)