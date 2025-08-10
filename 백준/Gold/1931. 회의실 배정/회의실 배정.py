import sys
from collections import deque
input = sys.stdin.readline

n= int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1],x[0]))
start = 0
result = 0

for schedule in lst:
    if schedule[0] >= start:
        start = schedule[1]
        result += 1

print(result)
