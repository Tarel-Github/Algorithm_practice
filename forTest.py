# 파이썬 코드 테스트를 위한 파일
N = list(input())

for i in range(len(N)):
    max = i
    for j in range(i+1, len(N)): # 최댓값 찾기
        if N[j] > N[max]:
            max = j# 최댓값이 위치한 인덱스
    if N[i] < N[max]:
        temp = N[i]
        N[i] = N[max]
        N[max] = temp

for i in range(len(N)):
    print(N[i])


