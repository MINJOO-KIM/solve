import sys
input = sys.stdin.readline
n,m = map(int, input().split())

names = {}
ids = {}
for i in range(1,n+1):
    name = input().rstrip()
    names[i] = name
    ids[name] = i
for _ in range(m):
    quiz = input().rstrip()
    if quiz.isalpha():
        print(ids[quiz])
    else:
        print(names[int(quiz)])