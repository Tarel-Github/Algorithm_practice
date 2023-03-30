import math

N = int(input())                # N과 서로소인 자연수를 구해야 함
result = N

for p in range(2, int(math.sqrt(N)) + 1):   #에라토스테네스처럼 제곱근까지만 진행,P는 2부터 N의 제곱근이다
    print('\n',p,'\n')
    if N % p == 0:                  # p가 N의 소인수(p로 N나눈 나머지가 0)라면
        print(result, N)
        result -= result / p        # 결과값(최대값의 복제)을 p로 나는 수를 result에서 뺀다.
        while N % p == 0:           # N % p == 0 이라는건 p가 N의 약수라는 뜻
            N /= p                  # N을 p로 나눈다.                            
        # N값은 지속적으로 작아지지만 for문의 범위에는 영향이 없다.

if N > 1:
    result -= result / N

print(int(result))

'''
이 부분은 암기가 나을듯 싶다.

'''