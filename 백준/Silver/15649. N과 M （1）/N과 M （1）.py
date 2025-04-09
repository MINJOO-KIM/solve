# 순열
n, l = map(int, input().split())
nums = []
for i in range(1,n+1):
    nums.append(i)
path=['']*l
used = [0]*n

def dfs(level):
    if level==l:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return
    for i in range(n):
        if used[i]==1: continue
        path[level]=nums[i]
        used[i]=1
        dfs(level+1)
        used[i]=0
dfs(0)