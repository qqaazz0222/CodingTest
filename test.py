def solution(num_list, n):
    answer = []
    nn = 0
    temp = []
    for i in range(num_list):
        if i == 0:
            temp.append(num_list(i))
        else:
            if i % n == 0:
                temp.append(num_list(i))
                answer.append(temp)
                temp = []
            else:
                temp.append(num_list(i))
    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
