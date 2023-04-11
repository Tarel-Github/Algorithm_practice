# 파이썬 코드 테스트를 위한 파일
checkList = [0] * 4     # [0, 0, 0, 0] -> 아래에서 ACGT의 제한사항이 됌
myList = [0] * 4        # [0, 0, 0, 0] -> 새로 만들 문자열에 ACGT가 각각 몇 개씩 있는지 확인하는 리스트
checkSecret = 0

# 함수 정의     # 기존 문자열의 i번째 숫자를 입력받고 그것이 해당하는 문자열ACGT에 해당하는게 1 늘어남
def myadd(c):   # 만약 해당 문자열이 필요한 수만큼 확보되면 checkSecret값이 1 증가한다.
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:   # 만약 A 문자열이 필요한 수만큼 확보되면 checkSecret값이 1 증가
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): # 제거되는 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())# 문자열 길이와 새로 만들 문자열 길이를 입력
Result = 0
A = list(input()) # 문자열을 입력 받음
checkList = list(map(int, input().split())) # ACGT의 제한사항을 배열로 입력받음

for i in range(4):          # 4번 반복
    if checkList[i] == 0:   # 제한사항중에 0인 것이 있다면
        checkSecret += 1    # 체크시크릿값을 1 증가

# 슬라이딩 윈도우의 최초위치를 만들기 위한 부분
for i in range(P):          # 새로만들 문자열 길이만큼 반복
    myadd(A[i])             # 기존 문자열의 i번째 숫자를 myadd함수에 투입
                            # 이 반복문을 통해, 새로 만들 문자열 길이에 ACGT가 각각 몇개씩 있는지 myList에 추가됌
if checkSecret == 4:
    Result += 1

for i in range(P, S):   # P는 새문자열길이, S는 기존문자열 길이다. 즉, 그 차이만큼 반복
    j = i - P           # P가 7, S가 10이라면 i가 7, 8, 9, 10일때 j는 0, 1, 2, 3, 4이다.
    myadd(A[i])         # 기존문자열에서 끝부분?에 해당하는 것들 가운데 ACGT가 있는것 만큼 숫자를 추가
    myremove(A[j])      
    if checkSecret == 4:
        Result += 1

print(Result)


# 주석 설명
"""
타겟이 되는 리스트를 받으면 우선 윈도우를 씌워야 한다.
예를 들어 리스트가 길이가 10이며 내용이
ACCAGTTGGT 이고 새로 만들 배열 길이가 5라면

최초의 윈도우는 ACCAG 를 감싸야 할 것이다.
55번 줄의 for 문이 바로 이 최초위치를 만들기 위한 부분이다.

윈도우를 감쌌으면 내부를 검사한다.
checkList는 사용자가 설정한 ACGT 수 제한이고
myList는 해당 윈도우에 포함된 ACGT의 수를 나타낸다.
만약 myList의 ACGT수가 checkList에 나타난 수치를 만족한다면
checkSecret의 값이 1증가한다.

고로 checkSecret의 값이 4라는 것은 곧 정답을 만족한다는 뜻
고로 result의 값이 1 증가한다.

이제 윈도우가 한칸씩 오른쪽으로 이동하고
그럴 때마다 myadd가 한 번씩 가동하여 myList 값이 올라가고
myremove도 발동하여 myList 값을 낮춘다.
myremove에서, 최종적으로 checkSecret의 값을 편집함으로써
한칸 오른쪽으로 이동한 이 경우도 만족하는지 알 수 있다.

"""