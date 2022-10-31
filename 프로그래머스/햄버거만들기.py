def solution(ingredient):
    answer = 0
    while True:
        print(ingredient)
        if len(ingredient) <= 4 and ingredient != [1, 2, 3, 1]:
            break
        for i in range(len(ingredient)-3):
            if ingredient[i] == 1:
                if ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
                    answer += 1
                    del ingredient[i: i+4]
                    break
    return answer


print(solution([1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1]))
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
