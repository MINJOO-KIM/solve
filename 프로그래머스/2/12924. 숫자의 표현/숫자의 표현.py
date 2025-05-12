def solution(n):
    answer = 0
    for i in range(1,n+1):
        c_sum = 0
        j = i
        while c_sum < n:
            c_sum+=j
            j+=1
        if c_sum == n:
            answer+=1
    return answer