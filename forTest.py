# 파이썬 코드 테스트를 위한 파일
N, n = map(int, input().split()) # 문자열 길이, 새로만든 문자열 길이

S = input() # 문자열
A, C, G, T = map(int, input().split()) #문자열 출연 조건

a = []
index = 0
count = 0
w = N - n

while 0 < w:
    for i in range(index, N):
        a.append(S[i])
    AC = a.count("A")
    CC = a.count("C")
    GC = a.count("G")
    TC = a.count("T")

    if AC >= A and CC >= C and GC >= G and TC >= T:
        count += 1
    index +=1
    w -= 1
    AC, CC, GC, TC = 0, 0, 0, 0

print(count)