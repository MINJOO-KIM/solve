import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(1,tc+1):
    n = int(input())
    categories = []
    # [headgear, eyewear]
    d = {}
    # {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}
    for _ in range(n):
        name, category = map(str, input().split())
        if category not in categories:
            categories.append(category)
            d[category] = []
            d[category].append(name)
        else:
            d[category].append(name)
    # 경우의 수 구하기
    result = 1
    for category in d:
        result *= (len(d[category])+1)
    result-=1
    print(result)
