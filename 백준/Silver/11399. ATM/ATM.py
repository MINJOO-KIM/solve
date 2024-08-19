n = int(input())
arr = list(map(int, input().split()))

arr.sort()

time=[0]*n
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    time[i]=sum

res = 0
for j in range(len(time)):
    res += time[j]

print(res)