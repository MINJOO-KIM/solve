lst = list(map(int,input()))
left, right = 0,0

for i in range(len(lst)):
    if i<len(lst)//2:
        right+=lst[i]
    else:
        left+=lst[i]
if right==left:
    print("LUCKY")
else:
    print("READY")