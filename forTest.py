# 임포트
import sys
input = sys.stdin.readline

# 데이터 입력
N =int(input())

# 리스트 준비, 단, DP 테이블이 아닌 1차원 배열
D = [-1]*(N+1)
D[0] = 0
D[1] = 1        # D는 0번 인덱스와 1번 인덱스를 제외한 모든 요소가 -1로 이루어진다.

# 피보나치 함수
def fibo(n):
    if D[n] != -1:
        return D[n]
    
    D[n] = fibo(n-2) + fibo(n-1)
    return D[n]

fibo(N)

print(D[N])


'''
'''