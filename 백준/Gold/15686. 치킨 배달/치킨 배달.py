from itertools import combinations

N,M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if lst[i][j]==2:
            chickens.append((i,j))
        elif lst[i][j]==1:
            houses.append((i,j))

combs = list(combinations(chickens,M))

distance = []
answer = 21e9

for comb in combs:
    total = 0

    for house in houses:
        Min = 21e9
        r1,c1 = house
        for chicken in comb:
            r2,c2 = chicken
            dist = abs(r1 - r2) + abs(c1 - c2)
            Min = min(Min, dist) 
        total+=Min
    answer = min(answer, total)
print(answer)