# 임포트
import sys
input = sys.stdin.readline

# 숫자 두 개를 입력 받는다.
N, K =map(int, input().split())

D = [[0 for j in range(N+1)] for i in range(N + 1)] # N X N 크기의 2차원 리스트 D를 생성

for i in range(0, N+1):
    D[i][1] = i     # 2차원 리스트 첫 가로줄의 값을 0, 1, 2, 3, 4....로 함
    D[i][0] = 1     # 2차원 리스트 
    D[i][i] = 1

for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i - 1][j-1]

print(D[N][K])
