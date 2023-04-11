# 최적화를 위한 임포트
import sys
input = sys.stdin.readline

# 몇 개의 숫자를 입력받는지를 입력하고, 수열을 입력
# 정답 변수를 선언하고 수열을 사용하기 좋게 정렬함
N = int(input())
A = list(map(int, (input().split())))
Result = 0
A.sort()

# 여기서부터 핵심
# 포인터 i와 j는 시작과 끝부분에서 시작한다.
# 이 두 포인터를 양쪽에서 조여나가는 식으로 전개한다.
# 목표값보다 작으면 시작포인터를, 크면 끝포인터를 당기는 방식이다.
for k in range(N):
    find = A[k]          # 목표값을 find로 저장
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:   # 목표값을 찾았을 때, 그 값이 자기자신인 경우는 제외해야 한다.
                Result += 1
                break
            elif i == k:    # 시작포인터나 끝포인터가 목표값이 되는 경우도 제외
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:    # 여기서부터는 포인터를 조여오는 구문
            i += 1
        else:
            j -= 1
print(Result)