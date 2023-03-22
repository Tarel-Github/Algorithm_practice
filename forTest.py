n = int(input())
A = list(map(int, (input().split())))

A.sort()
count = 0
i = 0
j = n-1 # 끝부분 인덱스가 마지막 번호에서 시작
tg = 0

while tg < n:
    if A[i] + A[j] > A[tg]:
        j -= 1
    elif A[i] + A[j] < A[tg]:
        i += 1
    else:   # 정답인 경우
        tg += 1
        count += 1
        i = 0
        j = n-1
    
    if j == 0:  # 없는 경우
        tg += 1
        i = 0
        j = n-1

print(count)