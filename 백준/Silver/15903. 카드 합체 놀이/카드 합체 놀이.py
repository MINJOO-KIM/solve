n,m = map(int, input().split())
arr = list(map(int, input().split()))

ans=0
for t in range(m):
    arr.sort()
    temp=arr[0]+arr[1]
    arr[0],arr[1]=temp,temp

for i in range(len(arr)):
    ans+=arr[i]
print(ans)
