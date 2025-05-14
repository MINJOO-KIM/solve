L, C = map(int, input().split())
arr = input().split()
arr.sort()
path = [''] * L
vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(level, start):
    if level == L:
        v = 0  # 모음 개수
        c = 0  # 자음 개수
        for ch in path:
            if ch in vowels:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            for ch in path:
                print(ch, end='')
            print()
        return

    for i in range(start, C):
        path[level] = arr[i]
        dfs(level + 1, i + 1)

dfs(0, 0)
