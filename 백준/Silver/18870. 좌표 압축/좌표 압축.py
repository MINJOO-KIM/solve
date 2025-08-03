import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

sorted_lst = sorted(lst)
order = 0
d = {}
temp = sorted_lst[0]
for i in range(n):
     if sorted_lst[i]!=temp:
         order+=1
         temp=sorted_lst[i]
     d[sorted_lst[i]]=order

for i in range(n):
    print(d[lst[i]],end=' ')