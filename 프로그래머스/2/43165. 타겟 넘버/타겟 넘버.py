def solution(numbers, target):
    global answer
    answer = 0
    def dfs(level, cur):
        if level==len(numbers):
            if cur == target:
                global answer
                answer+=1
            return
        dfs(level+1, cur-numbers[level])
        dfs(level+1, cur+numbers[level])
    dfs(0,0)
    return answer