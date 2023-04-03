# 임포트
import sys
input = sys.stdin.readline

# 노드 수를 입력받고 tree작성을 준비함
N = int(input())
tree = {}   # 딕셔너리 자료형, 입력예시기준으로 {'A': ['B', 'C'], 'B': ['D', '.']...} 이런 식으로 작성

# 트리 관계 입력받음, 루트, 왼쪽, 오른쪽 이런식으로
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

# 중간 왼쪽 오른쪽 (전위 순회)
def preOrder(now):
    if now == '.':
        return
    print(now, end= '')         # 순회중인 노드를 출력한다. 줄바꿈을 하지 않음

    preOrder(tree[now][0])      # 왼쪽 먼저
    preOrder(tree[now][1])      # 왼쪽이 끝나면 오른쪽

# 왼쪽 중간 오른쪽
def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])
    print(now, end= '')
    inOrder(tree[now][1])

# 왼쪽 오른쪽 중간
def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end= '')

print(tree)
preOrder('A')
print()
inOrder('A')
print()
postOrder('A')

