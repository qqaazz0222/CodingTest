def solution(arr1, arr2):
    answer = []+arr1
    for i in len(answer):
        for j in len(answer[i]):
            answer[i][j] = arr1[i][j] +
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
      [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
