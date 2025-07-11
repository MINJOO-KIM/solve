def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

n= int(input())
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

# x,y,z 축별로 좌표를 따로 담아서 각각 정렬 -> 인접노드 간 비용 edges에 넣기
x = []
y = []
z = []

for i in range(1,n+1):
    x1,y1,z1 = map(int, input().split())
    x.append((x1,i))
    y.append((y1,i))
    z.append((z1,i))

x.sort() # [(비용, 행성번호), (비용, 행성번호) ...]
y.sort()
z.sort()

edges = []
result = 0

for i in range(n-1): # 정렬된 인접행성끼리 비교
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는다면(부모노드 같지않을 때) 집합 연산 실행
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)