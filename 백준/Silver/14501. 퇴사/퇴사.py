n = int(input())
t = []
p = []
dp = [0]*(n+1)
for _ in range(n):
    x,y =map(int, input().split())
    t.append(x)
    p.append(y)
max_result = 0
for i in range(n-1,-1,-1):
    time = i + t[i]
    if time<=n:
        dp[i]=max(max_result,dp[time]+p[i])
        max_result=dp[i]
    else:
        dp[i]=max_result
print(max_result)