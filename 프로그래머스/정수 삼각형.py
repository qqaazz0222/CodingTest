def solution(triangle):
    answer = 0
    child = triangle.pop()
    while True:
        parent = triangle.pop()
        if len(parent) == 1:
            answer = max(parent) + max(child)
            break
        else:
            for i in range(len(parent)):
                parent[i] += max(child[i], child[i+1])
            child = parent

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
