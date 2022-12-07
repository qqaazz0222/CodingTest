def solution(priorities, location):
    answer = 1
    pS = []
    l = len(priorities)
    for i in range(len(priorities)):
        pS.append([priorities[i], i])
    while answer < l-1:
        print(priorities, pS)
        print(answer)
        if len(priorities) > 1:
            if priorities[0] >= max(priorities[1:]):
                if pS[0][1] == location:
                    return answer
                priorities = priorities[1:]
                pS = pS[1:]
                answer += 1
            else:
                priorities = priorities[1:] + [priorities[0]]
                pS = pS[1:] + [pS[0]]
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
