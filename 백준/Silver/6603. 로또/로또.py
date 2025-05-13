def dfs(level, start):
    if level == 6:
        for i in range(6):
            print(path[i], end=" ")
        print()
        return
    for i in range(start, k):
        path[level] = nums[i]
        dfs(level + 1, i + 1)
        
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    k = arr[0]
    nums = arr[1:]
    nums.sort()
    path = [''] * 6

    dfs(0, 0)
    print()