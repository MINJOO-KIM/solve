import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    action = input()
    n = int(input())
    lst = deque(eval(input()))
    r_flag = False
    e_flag = False

    for i in range(len(action)):
        if action[i]=='R':
            r_flag= not r_flag
        elif action[i]=='D':
            if len(lst)<=0:
                print('error')
                e_flag = True
                break
            if r_flag:
                lst.pop()
            else:
                lst.popleft()
    if not e_flag:
        if r_flag:
            lst.reverse()
        print('['+','.join(map(str,lst))+']')