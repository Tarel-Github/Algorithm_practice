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
        self.parent = Node(None)    # Node 클래스를 생성한다. 이는 공백상태의 루트노드가 된다.

    # 문자열 삽입
    # Apple 를 입력 받으면 A, p, p, l, e 가 전부 노드가 되며 앞글자가 뒷글자의 부모가 된다.
    # 이 상태에서 Air를 입력 받으면 i, r 노드가 생기고 이것이 A의 하위 노드가 된다.
    def insert(self, string):                             
        nowNode = self.parent       # 루트 노드부터 시작, Node를 생성한다.   
        temp_length = 0

        for char in string:         # 입력받은 문자열을 하나하나 입력한다. 예를들어, string이 'Apple' 이면 A, p, p...가 char에 담긴다.
            if char in string:
                if  char not in nowNode.childNode:          # 글자가 child노드에 없을 때
                    nowNode.childNode[char] = Node(char)    # 그 글자는 새로운 노드가 된다. 즉, 모든 노드에는 글자가 하나만 담긴다.
                
                nowNode = nowNode.childNode[char]           # 글자가 child노드에 없으면 위처럼 추가해서 nowNode에 넣고 있으면 바로 넣는다.
                temp_length += 1                            # 갈라져나가는 노드의 길이가 1씩 늘어난다.
                if temp_length == len(string):              # 노드 길이가 단어의 길이와 일치하다면
                    nowNode.isEnd = True                    # 이제 그 노드는 종료 노드가 된다.

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
        
# 입력을 받음, 먼저 등록할 문자 N개와 찾을 문자 M개
N, M = map(int , input().split())   # 먼저 사전에 등록할 문자열 N개를 받고 찾을 문자열 M개를 받음
myTrie = Trie()                     # Trie 클래스 사용
# 우선 등록할 문자를 입력받고 이를 트라이에 저장함
for _ in range(N):
    word = input().strip()          # 입력받은 문자열의 양쪽 끝의 공백을 제거
    myTrie.insert(word)             # Trie 클래스의 insert 함수에 word를 삽입

result = 0

# 찾을 문자를 입력받고 그걸 트라이에서 찾음, 있으면 result 1 증가
for _ in range(M):
    word = input().strip()
    if myTrie.search(word):
        result += 1

print(result)


'''

'''