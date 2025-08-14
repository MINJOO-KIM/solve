import sys
input = sys.stdin.readline

lst = []
n = int(input())
for _ in range(n):
    lst.append(int(input()))
lst.sort()
for i in lst:
    print(i)