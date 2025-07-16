n,m = map(int, input().split())
heard = set()
see = set()

for _ in range(n):
    heard.add(input())
for _ in range(m):
    see.add(input())

result = list(heard & see)

result.sort()
print(len(result))
for x in result:
    print(x)