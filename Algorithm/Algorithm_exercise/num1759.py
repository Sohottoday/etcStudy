# 문제 유형 : 백트래킹

# 문제
# 바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 
# 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
# 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
# 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. 
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 
# 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

# 출력
# 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

# 예제 입력 1 
# 4 6
# a t c i s w
# 예제 출력 1 
# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw


# 문제 풀이 핵심 아이디어
# c개의 문자가 주어졌을 때, 가능한 l길이의 암호를 모두 찾아야 한다.
# 따라서 c개의 문자들 중 l개를 선택하는 모든 조합을 고려해야 한다.
#   - Python의 조합(combinations) 라이브러리를 사용하면 간단히 해결 가능
#   - 혹은 DFS를 이용하여 조합 함수 구현 가능
# C=4, L=3 일 경우 4C3의 경우의 수이므로 총 4가지

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

# 가능한 암호를 사전식으로 출력해야 하므로 정렬 수행
array = input().split(' ')
array.sort()

# 길이가 1인 모든 암호 조합을 확인
for password in combinations(array, l):
    # 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    
    # 최소 한 개의 모음과 최소 두 개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))



#### dfs를 활용해 combinations 함수를 만들어 해결하는 경우
import copy
result = []
string = []
visited = []

# 조합(Combination) 함수 구현
def combination1(array1, length1, index1):
    # 길이가 length인 모든 조합 찾기
    if len(string) == length1:
        result.append(copy.deepcopy(string))
        return
    # 각 원소를 한 번씩만 뽑도록 구성
    for i in range(index1, len(array1)):
        if i in visited:
            continue
        string.append(array1[i])
        visited.append(i)
        combination1(array1, length1, i+1)
        string.pop()
        visited.pop()


vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

# 가능한 암호를 사전식으로 출력해야 하므로 정렬 수행
array = input().split(' ')
array.sort()

combination1(array, l, 0)

# 길이가 1인 모든 암호 조합을 확인
for password in result:
    # 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    
    # 최소 한 개의 모음과 최소 두 개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))