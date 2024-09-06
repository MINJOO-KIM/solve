n, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
start = arr[0]
ans = 1
for item in arr:
    if item >= start+l:
        ans+=1
        start = item
print(ans)