import sys
input = sys.stdin.readline
n,m = map(int, input().split())

dict = {}
for _ in range(n):
    site, password = map(str, input().split())
    dict[site] = password

for _ in range(m):
    quiz = input().rstrip()
    print(dict[quiz])