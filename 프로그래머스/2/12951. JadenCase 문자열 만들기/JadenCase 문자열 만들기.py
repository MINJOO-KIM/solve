def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        if arr[i]:  
            arr[i] = arr[i][0].upper() + arr[i][1:].lower()
    return ' '.join(arr)