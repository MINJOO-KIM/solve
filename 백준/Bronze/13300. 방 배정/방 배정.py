n,k = map(int, input().split())
arr = [[0]*2 for _ in range(7)]
for i in range(n):
    s,y = map(int, input().split())
    arr[y][s]+=1

ans = 0

for i in range(7):
    for j in range(2):
        if arr[i][j]%k==0:
            ans+=arr[i][j]//k
        else:
            ans+=arr[i][j]//k+1

print(ans)