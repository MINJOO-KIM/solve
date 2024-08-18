n,k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
result = 0
for j in coins:
    result += k//j
    k = k % j

print(result)