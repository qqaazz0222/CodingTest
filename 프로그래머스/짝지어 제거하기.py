def solution(s):
    answer = 0
    stack = ['0']
    for i in s:
        if stack[-1] == i:
            del stack[-1]
        else:
            stack.append(i)
    if stack == ['0']:
        answer = 1
    return answer


print(solution("baabaa"))
print(solution("cdcd"))
