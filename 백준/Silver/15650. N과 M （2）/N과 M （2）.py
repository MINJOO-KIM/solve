# 조합
n, l = map(int, input().split())
nums = []
for i in range(1,n+1):
    nums.append(i)
path=['']*l

def dfs(level,start):
    if level==l:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return
    for i in range(start,n):

        path[level]=nums[i]

        dfs(level+1,i+1)

dfs(0,0)