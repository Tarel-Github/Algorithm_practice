# 임포트
import sys
input = sys.stdin.readline

# 리스트의 크기와 질의 수를 입력
n, m = map(int, input().split())

'''
아래 A는 만약 n이 5면 다음과 같이 나온다. 보시다시피 한 칸 더 나온다.
A = [[0, 0, 0, 0, 0, 0]]

D 는 아래와 같이 나온다. 마찬가지로, 행렬 각각 한 칸 더 나온다.
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

'''
A = [[0] * ( n + 1 )]
D = [[0] * ( n + 1 ) for _ in range(n+1)]           # [[0] * ( n + 1 )] * (n + 1) 이렇게 적어도 됌

# 각 배열들의 요소를 입력받아서 2차원 배열을 완성하기 위한 부분
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

print(A)
print(D)
# 이곳이 핵심, 2차원 합배열을 완성하는 반복문이다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 어디서부터 어디까지 더할지를 입력받는다.
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
 
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1 - 1][y1 - 1]
    print(result)