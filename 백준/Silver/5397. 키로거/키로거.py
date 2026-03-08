for _ in range(int(input())):
    left = []
    right = []
    s = input()
    for command in s:
        if command=='<':
            if left:
                right.append(left.pop())
        elif command=='>':
            if right:
                left.append(right.pop())
        elif command=='-':
            if left:
                left.pop()
        else:
            left.append(command)

    print("".join(left+right[::-1]))