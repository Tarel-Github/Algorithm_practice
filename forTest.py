n, m = list(map(int, input().split()))
A = [[0]* (n + 1)]
D = [[0]* (n + 1) for i in range(n + 1)]
#[0]* (n + 1) 이건 [0]을 (n+1)만큼 넣으라는 의미, 즉 [0 ,0 ...., n]이 된다.
# n은 배열의 크기, m은 질문의 수가 된다.

a = []
for i in range(0, n + 1):
    a.append(i)
D[0] = a
# 첫번째 행을 0, 1, 2, 3, 4~로 채운다

for i in range(n):
    A_row = [i] + list(map(int, input().split()))
    D[i+1] = A_row
# 2차원 배열을 완성
print(D)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]


for _ in range(m):
    x1, y1, x2, y2 = list(map(int, input().split()))
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)