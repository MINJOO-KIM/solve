n = int(input())
lst = list(map(int, input().split()))

answer = 0
left = 0
cnt = {}
fruit_cnt = 0

for right in range(n):
    if lst[right] in cnt:
        cnt[lst[right]] += 1
    else:
        cnt[lst[right]] = 1
        fruit_cnt += 1

    while fruit_cnt > 2:
        cnt[lst[left]] -= 1
        if cnt[lst[left]] == 0:
            del cnt[lst[left]]
            fruit_cnt -= 1
        left += 1

    answer = max(answer, right - left + 1)

print(answer)