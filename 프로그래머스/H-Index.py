def solution(citations):
    answer = 0
    n = len(citations)
    h = 1
    while True:
        if h > n:
            break
        temp = 0
        for i in citations:
            if i >= h:
                temp += 1
        if temp >= h:
            answer = h
        h += 1
    return answer


# print(solution([4, 4, 4]))
print(solution([3, 0, 6, 1, 5]))
# print(solution([1, 2, 3, 4, 5]))
# print(solution([1, 1, 1, 2, 4, 6, 8, 10]))
# print(solution([0, 0, 0, 0]))
