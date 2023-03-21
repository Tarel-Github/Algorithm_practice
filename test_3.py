# 구간 합
# 내 답안
n = list(map(int, input().split()))
target =list(map(int, input().split()))
porpose = list(map(int, input().split()))
sum = 0

for i in range(porpose[0]-1, porpose[1]):
    print(porpose[0]-1)
    print('아이값',i, target[i])
    sum += target[i]

print(sum)