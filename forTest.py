n = int(input())            # 수가 몇 개인지 입력
ans = [0] * n               # 수의 개수길이 만큼 리스트를 준비, 이건 정답용
A = list(map(int, input().split())) # 리스트를 완성
myStack = []                # 스텍을 준비, 이 스텍은 인덱스보다 높은 값을 저장하는 역할을 한다.

for i in range(n):          
    print(i, myStack, A, ans)
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""

for i in range(n):
    result += str(ans[i]) + " "

print(result)