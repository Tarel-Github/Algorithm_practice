import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())    # 노드와 엣지의 수를 입력받는다.
A = [[] for _ in range(n + 1)]      # 리스트 안에 노드 수 + 1 개만큼 추가로 빈 리스트를 만든다.
visited = [False] * (n + 1)         # 위와 똑같이 만든다. 단, 안에 False가 있어야 한다.

def DFS(v):
    visited[v] = True   # 함수가 실행되었다는건 해당 요소에 방문을 했다는 뜻
    for i in A[v]:      # A배열의 V번째 리스트의 요소를 빼서 i에 대입하며 반복
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())    # 뭐랑 뭐가 연결된 엣지인지 차례대로 입력받는다.
    A[s].append(e)                      # A행렬의 s번째에 e가 대입된다.
    A[e].append(s)                      # 반대로도 적용한다. 
                        # 이걸 반복하면 s번째 노드는 e와 연결되어 있다는 데이터가 담긴 배열이 완성된다.
print(A)
count = 0

for i in range(1,n+1):
    if not visited[i]:  # 우선 visited의 모든 요소가 False이므로 이 조건문을 통과한다.
        count += 1      # count가 1 증가하고 주 함수 실행
        DFS(i)
print(A, visited)
print(count)

'''A리스트는 1부터 N+1개의 요소를 가지고 있다.
    1번 인덱스에 2와 5의 값을 가지고 있다면 이는 1번 노드는 2번과 5번 노드와 연결되어 있다는 의미다.
    당연히 0번 인덱스는 없는셈 친다.

    때문에 1 ~ n+1 동안 반복문을 돌린다.
    
    노드 방문 여부를 체크하는 리스트에서, 해당 리스트 값이 False라면 DFS 함수를 실행한다.
    그리곤 해당 리스트 값을 True로 바꾼다.
    A리스트의 해당 인덱스 값은 자신과 이어진 노드 번호를 뜻하니
    visited 리스트에서 False인 인덱스를 찾아서 다시 DFS 함수를 돌린다.
    이렇게 재귀함수 처럼 사용하면 해당 인덱스의 끝까지 방문할 수 있다.

    DFS가 끝났을 때, 아직 방문하지 않은 노드가 있다면 다서 DFS를 실행하고
    count값이 오른다.
    '''