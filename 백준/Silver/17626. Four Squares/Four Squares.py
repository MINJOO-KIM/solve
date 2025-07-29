import sys
input = sys.stdin.readline
n = int(input())
INF = int(1e9)
dp = [INF]*(n+1)
dp[0]=0
for i in range(n+1):
    j = 1
    while j**2 <= i:
        dp[i]=min(dp[i],dp[i-j*j]+1)
        j+=1
print(dp[n])