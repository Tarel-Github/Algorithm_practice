import sys
sys.setrecursionlimit(10**6)        # 최대 재귀 깊이를 설정하는것, 기본적으로 1000번까지만 재귀하지만 여기선 더 깊게 설정한다.
input = sys.stdin.readline

N = int(input())            # 노드 개수를 입력 받음

visited = [False] * (N + 1)             # 방문 여부 리스트, 0번은 안 쓰고 False로 체운다.
tree = [[]for _ in range(N + 1)]        # 노드 수 + 1개만큼 배열안의 배열을 만듦

answer = [0] * (N + 1)                  # 정답 리스트, [0, 0, 0, 0......] 형태로 만듦

for _ in range(1, N):
    n1, n2 = map(int, input().split())  # 노드 연결 정보를 입력 받아서
    tree[n1].append(n2)                 # n1번에 n2를, n2번에 n1값을 넣는다.
    tree[n2].append(n1)                 # 이건 방향이 없기 때문에, 2차원 배열이 대각선 대칭이 되기 때문이다.

# DFS 함수
def DFS(number):                        # 재귀 형태로 찾음
    visited[number] = True
    for i in tree[number]:
        if not visited[i]:
            answer[i] = number
            DFS(i)

DFS(1)                                  # DFS 탐색 시작

# 출력
for i in range(2, N+1):
    print(answer[i])

'''

'''