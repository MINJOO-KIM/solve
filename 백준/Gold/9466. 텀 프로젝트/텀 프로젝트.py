import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = True
    next = nums[x]

    # 방문 안했으면 계속 탐색
    if not visited[next]:
        dfs(next)
    # 방문했으면 사이클 있는지 확인하기
    else:
        if not finished[next]:  # 사이클 발견
            cur = next
            cycle_size = 1
            while cur != x:
                cur = nums[cur]
                cycle_size += 1
            cnt += cycle_size

    finished[x] = True  # 탐색 끝 표시

for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    finished = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    print(n - cnt)
