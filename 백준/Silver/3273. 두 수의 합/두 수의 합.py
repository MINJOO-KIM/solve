import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
left, right = 0, n-1
while left < right:
    num = arr[left] + arr[right]
    if (num == x):
        cnt +=1
        left += 1
    elif num < x:
        left += 1
    else:
        right -= 1
        
print(cnt)