import sys
input = sys.stdin.readline
n = int(input())
lst =[]
for i in range(n):
    age,name = input().split()
    age = int(age)
    lst.append((age,name))
lst.sort(key=lambda x: x[0])
for user in lst:
    print(user[0],user[1])