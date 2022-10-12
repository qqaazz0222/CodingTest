def solution(priorities, location):
    answer = 0
    target = priorities[location]
    result = []
    while True:
        if priorities == []:
            break
        else:
            temp = priorities[0]
            if temp < max(priorities):
                priorities.append(temp)
            else:
                result.append(temp)
            del priorities[0]
    answer = result.index(target)
    print(target, result)
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))