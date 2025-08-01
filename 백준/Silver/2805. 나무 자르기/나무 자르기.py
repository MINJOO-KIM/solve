import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

start = 0
end = max(lst)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2

    for x in lst:
        # 잘랐을 때
        if x>mid:
            total += x-mid
    # 더 잘라야할 때
    if total<m:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)
