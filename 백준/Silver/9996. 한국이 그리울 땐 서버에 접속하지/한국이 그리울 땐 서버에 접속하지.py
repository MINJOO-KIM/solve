N = int(input())
start, end = input().split('*')

for _ in range(N):
    name = input()

# 반례) 파일 이름이 패턴보다 짧을 때
    if len(start)+len(end)>len(name):
        print('NE')
    else:
        if start == name[:len(start)] and end == name[-(len(end)):]:
            print('DA')
        else:
            print('NE')