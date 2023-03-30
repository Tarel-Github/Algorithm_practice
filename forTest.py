a, b, c = map(int, input().split())

def gcd(a,b):           # 최대 공약수 구하는 알고리즘
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def Execute(a, b):
    ret = [0] * 2               # [0,0] 배열을 만듦
    if b == 0:                  # ax+by=c 식에서 bx가 0이 되는 경우로 이때는 [1, 0]만 하고 바로 리턴
        ret[0] = 1              # 단, 재귀로 돌아온 경우, a % b가 0이면 이쪽으로 온다.
        ret[1] = 0
        return ret
    q = a // b
    v = Execute(b, a % b)       # b와 ab최.공을 넣고 다시 재귀 시작, 어느순간 [1, 0]을 반환받는 순간이 있다.
    ret[0] = v[1]
    ret[1] = v[0] - v[1] * q
    return ret


mgcd = gcd(a, b)        # 최대공약수를 구해옴

if c % mgcd != 0:       # c가 최대공약수로 안 나뉘어지면 불가능 리턴
    print(-1)
else:
    mok = int(c / mgcd)               # mok은 C/최.공
    ret = Execute(a, b)
    print(ret[0] * mok, end = ' ')
    print(ret[1] * mok)


'''

'''