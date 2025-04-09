n, l = map(int, input().split())
nums = []
for i in range(1,n+1):
    nums.append(i)
path=['']*l

def dfs(level):
    if level==l:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return
    for i in range(n):

        path[level]=nums[i]

        dfs(level+1)

dfs(0)