from collections import deque
n,k = map(int, input().split())
q = deque()
for i in range(n):
    q.append(i+1)
ans = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    else:
        ans.append(q.popleft())
result = ", ".join(map(str,ans))
print(f"<{', '.join(map(str,ans))}>")