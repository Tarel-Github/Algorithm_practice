import sys
from queue import PriorityQueue

input = sys.stdin.readlines
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * ( N + 1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] =find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N - 1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)


'''

'''