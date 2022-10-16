def solution(arrows):
    answer = 0
    point = [0, 0]
    route = [[0, 0]]
    for i in arrows:
        temp = []
        if i == 0:
            point[1] += 1
        elif i == 1:
            point[0] += 1
            point[1] += 1
        elif i == 2:
            point[0] += 1
        elif i == 3:
            point[0] += 1
            point[1] -= 1
        elif i == 4:
            point[1] -= 1
        elif i == 5:
            point[0] -= 1
            point[1] -= 1
        elif i == 6:
            point[0] -= 1
        elif i == 7:
            point[0] -= 1
            point[1] += 1
        temp = [point[0], point[1]]
        if temp in route:
            answer += 1
            print(temp, route)
        route.append(temp)
    return answer


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))
