def dfs(idx, result, numbers, target):
    global answer

    if idx == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(idx + 1, result + numbers[idx], numbers, target)
    dfs(idx + 1, result - numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    answer = 0  
    dfs(0, 0, numbers, target)
    return answer
