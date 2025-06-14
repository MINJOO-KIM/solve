n = int(input())
lst = list(map(int, input().split()))
cnt = 0

lst.sort()

while len(lst)>1:
  lst[0]-=1
  lst.pop() # 마지막 요소 제거
  if lst[0]==0:
   lst.pop(0)
  cnt+=1
print(cnt)