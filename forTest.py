import sys
input = sys.stdin.readline


N = int(input())                    # 도시 수 입력
M = int(input())                    # 노선 수 입력(이 문제에선 노선 수만큼 반복)

# 거리 배열을 엄청 큰 수를 바탕으로 초기화, 0번 인덱스는 사용하지 않음
distance=[[sys.maxsize for j in range(N+1)] for i in range(N+1)]
#print(distance) #[[최대값, 최대값...], [최대값, 최대값...]]  // 안의 요소는 N+1개, 배열 수는 N+1

# 각각 대각선 배열에 해당하는 부분을 0으로 초기화 예를 들어, 아래와 같음
# [[1], [1], [1], [1]]
# [[1], [0], [1], [1]]
# [[1], [1], [0], [1]]
# [[1], [1], [1], [0]]......      편의상 1을 입력했지만, 실제론 가장 큰 값이 들어가 있음
for i in range(1, N+1):
    distance[i][i] = 0

# 연결 정보를 받는 구간, s는 출발점, e는 도착점, v는 가중치다.
for i in range(M):
    s, e, v = map(int, input().split())
    if distance[s][e] > v:      # 위 예시 배열에서, s,e 의 지점 값이 가중치 보다 크다면 가중치 값으로 바꾼다.
        distance[s][e] = v      # 이런 조건이 있는 이유는 자기자신인 '0으로 초기화된 값'은 예외로 하기 위함이다.

# 여기까진 필요한 자료를 준비하는 과정
print(distance)
# 플로이드 - 워셜 수행
for k in range(1, N+1):             # k는 경유지
    for i in range(1, N+1):         # i는 출발지
        for j in range(1, N+1):     # j는 도착지
            #print(k, i, j)
            # "i출발 j도착" 거리가  "i출발 k 경유 j 도착"보다 크다면
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end= ' ')
    print()

'''

'''