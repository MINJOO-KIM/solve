n= int(input())
arr = []
for _ in range(n):
    a,b,c,d = map(int, input().split())
    a*=100
    c*=100
    arr.append([a+b,c+d])
arr.sort(key=lambda x:(x[0],x[1]))
cnt=0
end=0
start=301

while arr:
    if start>1130 or start<arr[0][0]:break

    for _ in range(len(arr)):
        if start>=arr[0][0]:
            if end<=arr[0][1]:
                end=arr[0][1]
            arr.remove(arr[0])
        else:
            break
    start = end
    cnt+=1
if start<=1130:
    print(0)
else:
    print(cnt)