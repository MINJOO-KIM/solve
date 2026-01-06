cnt = 0
def solution(num, target):
    global cnt
    # print(num)
    n = len(num)    
    def dfs(level, res):
        # print(res)
        global cnt
        if level==n:
            if res == target:
                cnt+=1
            return
        for i in range(2):
            dfs(level+1,res+num[level]*(-1)**(i+1))
    
    dfs(0,0)
    
    answer = cnt
    return answer