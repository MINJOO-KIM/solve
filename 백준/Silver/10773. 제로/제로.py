s = []
ans = 0
for _ in range(int(input())):
    n = int(input())
    if n!=0:
        s.append(n)
    else:
        if s:
            s.pop()
for i in s:
    ans += i
print(ans)
