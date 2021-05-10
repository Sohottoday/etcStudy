# 문제
# With plenty of free time on their hands (or rather, hooves), 
# the cows on Farmer John's farm often pass the time by playing video games. 
# One of their favorites is based on a popular human video game called Puyo Puyo; the cow version is of course called Mooyo Mooyo.

# The game of Mooyo Mooyo is played on a tall narrow grid  cells tall () and 10 cells wide. 
# Here is an example with :

# 0000000000
# 0000000300
# 0054000300
# 1054502230
# 2211122220
# 1111111223
# Each cell is either empty (indicated by a 0), or a haybale in one of nine different colors (indicated by characters 1..9). 
# Gravity causes haybales to fall downward, so there is never a 0 cell below a haybale.

# Two cells belong to the same connected region if they are directly adjacent either horizontally or vertically, 
# and they have the same nonzero color. Any time a connected region exists with at least  cells, 
# its haybales all disappear, turning into zeros. 
# If multiple such connected regions exist at the same time, they all disappear simultaneously. 
# Afterwards, gravity might cause haybales to fall downward to fill some of the resulting cells that became zeros. 
# In the resulting configuration, there may again be connected regions of size at least  cells. 
# If so, they also disappear (simultaneously, if there are multiple such regions), 
# then gravity pulls the remaining cells downward, and the process repeats until no connected regions of size at least  exist.

# Given the state of a Mooyo Mooyo board, please output a final picture of the board after these operations have occurred.

# 입력
# The first line of input contains  and  (). The remaining  lines specify the initial state of the board.

# 출력
# Please output  lines, describing a picture of the final board state.
# 예제 입력 1 
# 6 3
# 0000000000
# 0000000300
# 0054000300
# 1054502230
# 2211122220
# 1111111223
# 예제 출력 1 
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 1054000000
# 2254500000
# 힌트
# In the example above, if , then there is a connected region of size at least  with color 1 and also one with color 2. 
# Once these are simultaneously removed, the board temporarily looks like this:

# 0000000000
# 0000000300
# 0054000300
# 1054500030
# 2200000000
# 0000000003
# Then, gravity takes effect and the haybales drop to this configuration:

# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 1054000300
# 2254500333
# Again, there is a region of size at least  (with color 3). Removing it yields the final board configuration:

# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 1054000000
# 2254500000


def new_array(N):
    return[[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())

M = [list(input()) for _ in range(N)]

ck = new_array()

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or dfs[x][y] != dfs[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret

def dfs2(x, y, val):
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[xx][yy] != val:
            continue
        ret += dfs(xx, yy)
    return ret

def down(x, y):
    pass

while True:
    exist = True
    ck = new_array()
    for i in range(N):
        for j in range(10):
            if M[i][j] == 0 or ck[i][j]:
                continue
            res = dfs(i, j)


    if exist:
        break

for i in M:
    print(''.join(i))


# 해당 문제에 대한 고찰 필요
