# 임포트
import sys
input = sys.stdin.readline

# 좌표 포인트를 입력 받음
x1, y1 = map(int, input.split())
x2, y2 = map(int, input.split())
x3, y3 = map(int, input.split())

# CCW 공식을 그대로 사용
result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

# 양수면 시계방향, 음수면 반 시계방향, 0이면 직선이다.
if result > 0:
    print(1)   
elif result < 0:
    print(-1)
else:
    print(0)