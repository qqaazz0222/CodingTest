import math

def solution(progresses, speeds):
    stack = []
    answer = []
    for i in range(len(progresses)):
        temp = math.ceil((100 - progresses[i])//speeds[i])
        if len(stack) == 0:
            stack.append(temp)
        else:
            before = stack.pop()
            stack.append(before)
            if before > temp:
                stack.append(before)
            else:
                stack.append(temp)
    
    ss = list(dict.fromkeys(stack))
    print(ss)
    for i in ss:
        answer.append(stack.count(i))
    return answer

print(solution([95], [3]))