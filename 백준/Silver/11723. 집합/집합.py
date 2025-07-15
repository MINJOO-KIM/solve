import sys
input = sys.stdin.readline
arr = []

for _ in range(int(input())):
    operation_input = list(input().split())
    operation = operation_input[0]
    if len(operation_input)>1:
        num = int(operation_input[1])
    else:
        num = None
    if operation=='add':
        if num in arr:
            pass
        else:
            arr.append(num)
    elif operation=='check':
        if num in arr:
            print(1)
        else:
            print(0)
    elif operation=='remove':
        if num in arr:
            arr.remove(num)
        else:
            pass
    elif operation=='toggle':
        if num in arr:
            arr.remove(num)
        else:
            arr.append(num)
    elif operation=='all':
        arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif operation=='empty':
        arr = []
