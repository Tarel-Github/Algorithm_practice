n = int(input())
mylist = list(map(int, input().split()))
maxValue = max(mylist)
print((sum(mylist)* 100/ maxValue) / n )