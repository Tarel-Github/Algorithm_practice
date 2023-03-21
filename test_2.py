# 내 답안
# 형변환을 빼먹지 말 것, 입력받은 값은 문자열판정
n = input()
score = input().split(' ')
score.sort()
newScore = []
top = int(score[-1])
ans = 0
for i in score:
    newScore.append(int(i) / top * 100)
    print(newScore)
for i in newScore:
    ans += i

print(ans/len(score))

# 책의 답안
# 반복문 없이 풀었다,
n = input()
mylist = list(map(int, input().split()))
mymax= max(mylist)
sum = sum(mylist)
print(sum * 100 / mymax / int(n))

# 나의 문제점
# 높은 for문 의존도
# 낮은 형변환 활용도