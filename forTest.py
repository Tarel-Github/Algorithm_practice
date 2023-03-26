# 파이썬 코드 테스트를 위한 파일
from collections import deque
N = int(input()) # 카드 수 입력
myQueue = deque()

for i in range(N):
    myQueue.append(i+1)

while len(myQueue):
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])