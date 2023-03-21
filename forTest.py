n = int(input())
count = 1           # 리턴해야할 값, 총 몇 종류가 나오는가?
start_index = 1
end_index = 1
sum = 1             # 더하는 값 저장

while end_index != n:
    if sum == n:        # 정답인 경우
        count += 1
        end_index += 1
    elif sum > n:       # 두 포인터 사이 값을 전부 더했을 때, n보다 크다면
        sum -= start_index  # 
        start_index += 1    # 스타트 값을 올린다.
    else:               # 두 포인터 사이 값이 n보다 작다면(초반부에 주로 발생)
        end_index += 1
        sum += end_index

print(count)