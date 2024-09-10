n = int(input())
m = int(input())

arr = [[0]*n for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
    arr[j-1][i-1] = 1

friends = []

for j in range(n):
    if arr[0][j] == 1:
        friends.append(j)
        for i in range(n):
            if arr[j][i] == 1 and i != 0 and i not in friends:
                friends.append(i)

ans=set(friends)

if ans:
    print(len(ans))
else:
    print(0)
