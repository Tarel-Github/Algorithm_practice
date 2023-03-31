import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # 도시수, 도로수, 구할 거리, 출발 도시 번호
A = [[] for _ in range(N+1)]        # 0번 인덱스는 버리기 때문에 N+1번 수행
answer = []
visited = [-1] * (N + 1)            # 0번 인덱스는 버리는듯 함


# BFS 탐색 함수, 전에 사용한 BFS알고리즘이랑 거의 일치한다. print()위치와 visited 만 다르다.
def BFS(v):
    queue = deque()
    queue.append(v)         # 큐에 출발도시번호 삽입
    visited[v] += 1         # 출발 도시는 0으로 변경, 나머지는 -1
    while queue:
        now_Node = queue.popleft()      # 큐에서 왼쪽 값을 빼고 now_Node에 삽입
        for i in A[now_Node]:           # 예를들어, A[1]가 [1, 2, 3] 이면 1, 2, 3 순차로 가져옴
            if visited[i] == -1:        # 방문한 적이 없다면
                visited[i] = visited[now_Node] + 1  # 방문 기록을 1 올린다.
                queue.append(i)         # 큐에 방문한 노드들을 추가한다.

# 노드 연결 정보를 입력받고 A배열의 S번째 인덱스에 E를 넣는다.
# 즉, 각 도시가 어디랑 연결되어 있는지 인덱스와 요소로써 나타낸다.
for _ in range(M):
    S, E =map(int, input().split())
    A[S].append(E)

BFS(X)              # 출발 도시 번호로 BFS 탐색 시작
print(visited)      # BFS는 visited를 반환한다.

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)

'''

'''