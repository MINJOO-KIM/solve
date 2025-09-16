n= int(input())
cards = list(map(int, input().split()))
m = int(input())
questions = list(map(int, input().split()))

dict = {}
for card in cards:
    if card in dict:
        dict[card]+=1
    else:
        dict[card]=1

for target in questions:
    if target in dict:
        print(dict[target],end=" ")
    else:
        print(0, end=" ")
