import sys
input = sys.stdin.readline

arr = set()

for _ in range(int(input())):
    parts = input().split()
    op = parts[0]
    num = int(parts[1]) if len(parts) > 1 else None

    if op == 'add':
        arr.add(num)
    elif op == 'check':
        print(1 if num in arr else 0)
    elif op == 'remove':
        arr.discard(num)
    elif op == 'toggle':
        if num in arr:
            arr.remove(num)
        else:
            arr.add(num)
    elif op == 'all':
        arr = set(range(1, 21))
    elif op == 'empty':
        arr = set()
