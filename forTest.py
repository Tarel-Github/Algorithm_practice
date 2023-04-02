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
        self.isEnd = isEnd      # 마지막 노드
        self.childNode={}       # 자식 노드를 저장하는 딕셔너리

# 트라이 클래스
class Trie(object):
    def __init__(self):
        self.parent = Node(None)    # Node 클래스를 생성하고, isEnd에는 아무것도 전달되지 않으므로 마지막 노드가 아니라는 뜻이다

    # 문자열 삽입
    def insert(self, string):                             
        nowNode = self.parent       # 루트 노드부터 시작     
        temp_length = 0

        for char in string:         # 입력받은 문자열을 하나하나 입력한다. 예를들어, string이 'Apple' 이면 A, p, p...가 char에 담긴다.
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
N, M = map(int , input().split())   # 먼저 사전에 등록할 문자열 N개를 받고 찾을 문자열 M개를 받음
myTrie = Trie()                     # Trie 클래스 사용

for _ in range(N):
    word = input().strip()          # 입력받은 문자열의 양쪽 끝의 공백을 제거
    myTrie.insert(word)             # Trie 클래스의 insert 함수에 word를 삽입

result = 0

for _ in range(M):
    word = input().strip()
    if myTrie.search(word):
        result += 1

print(result)


'''

'''