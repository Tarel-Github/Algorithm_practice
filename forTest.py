# 항상 해오던 아래 코드는 없어도 된다.
# import sys
# input = sys.stdin.readline()

# 디큐를 사용
from collections import deque       # 디큐 키워드는 deque로 dequeue가 아님을 주의
N, L = map(int, input().split())      # N은 숫자의 수, L은 윈도우 길이
mydeque = deque()                     # 디큐를 윈도우로 사용
now = list(map(int, input().split()))



# 여기서부터 핵심, 숫자만큼 반복
for i in range(N):
    # mydeque에 값이 있는지부터 확인한다. 없으면 스킵, -1은 가장 오른쪽 값을 뜻한다
    # 즉 mydeque의 가장 오른쪽에 있는 값(인덱스아님)이 초기 배열의 i 번째 값보다 크면
    # 가장 오른쪽의 값을 빼낸다. 조건을 만족하면 전부 빼야하기 때문에 while문 사용
    while mydeque and mydeque[-1][0] > now[i]:      
        mydeque.pop()           
    mydeque.append((now[i], i))                 # 리스트의 i번째칸에 튜플을 삽입한다. now[i]는 리스트값, i는 인덱스 값이다.
    if mydeque[0][1] <= i - L:  
        mydeque.popleft()                       # 디큐의 왼쪽을 빼낸다.
    print(mydeque[0][0], end = ' ')              # 정답 출력, 줄바꿈 없이

"""
mydeque 에 now 리스트 값을 (값, 인덱스)로 형태로 하나씩 넣는다.
mydeque 의 길이가 L(윈도우 길이)를 벗어나면 왼쪽 것을 빼낸다.
그 다음 가장 왼쪽의 값을 

"""