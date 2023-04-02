# 임포트
from sys import stdin
input = stdin.readline

# 필요한건 다음과 같다.
# 노드에 대한 정의
# 트라이에 대한 정의
# 트라이에서, 문자열을 추가
# 트라이에서, 문자열을 찾기

# 노드 클래스
class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode={}

# 트라이 클래스
class Trie(object):
    def __init__(self):
        self.parent = Node(None)

    # 문자열 삽입
    def insert(self, string):                             
        nowNode = self.parent   
        temp_length = 0
        for char in string:
            if char in string:
                if  char not in nowNode.childNode:
                    nowNode.childNode[char] = Node(char)
                
                nowNode = nowNode.childNode[char]
                temp_length += 1
                if temp_length == len(string):
                    nowNode.isEnd = True
                    
    # 문자가 존재하는지 검색
    def search(self, string):                               
        nowNode = self.parent
        temp_length = 0
        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                temp_length += 1
                if temp_length == len(string) and nowNode.isEnd == True:
                    return True
                else:
                    return False
            return False
        
# 입력을 받음
N, M = map(int , input().split())
myTrie = Trie()

for _ in range(N):
    word = input().strip()
    myTrie.insert(word)

result = 0

for _ in range(M):
    word = input().strip()
    if myTrie.search(word):
        result += 1

print(result)


'''

'''