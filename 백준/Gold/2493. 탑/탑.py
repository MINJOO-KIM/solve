import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

s = [[arr[0],0]]
ans = [0]

for i in range(1,n):
    while s and s[-1][0] < arr[i]:
        s.pop()
    if s:
        ans.append(s[-1][1]+1)
    else:
        ans.append(0)

    s.append([arr[i],i])

print(*ans)