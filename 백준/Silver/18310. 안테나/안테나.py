n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값
print(a[(n - 1) // 2])