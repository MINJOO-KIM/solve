n = int(input())
arr = list(map(int, input().split()))
ans = int(input())
cnt=0

arr.sort()
start,end = 0,n-1

while start<end:
    hap=arr[start] + arr[end]
    if hap==ans:
        start+=1
        cnt+=1
    elif hap<ans:
        start+=1
    else:
        end-=1
print(cnt)