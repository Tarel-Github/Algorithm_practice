# 파이썬 코드 테스트를 위한 파일
N = int(input())
A = list(map(int, input().split()))
S = []
result = 0
sum = 0

for i in range(0, len(A)):
    S.append(A[i])
    for j in range(0, len(S)):
        if S[i] < S[j]:
            temp = S[j]
            S[j] = S[i]
            S[i] = temp

# 여기까지 정렬 완료
for i in A:
    result += i
    sum += result
    print(result, sum)

