def solution(arr1, arr2):
    answer = []
    arr1Data = {
        'r' : len(arr1[0]),
        'c' : len(arr1)
    }
    arr2Data = {
        'r' : len(arr2[0]),
        'c' : len(arr2)
    }
    for c1 in range(arr1Data['c']):
        temp = []
        for r1 in range(arr1Data['r']):
            n = 0
            for c2 in range(arr2Data['c']):
                n += (arr1[c1][c2]*arr2[c2][r1])
            temp.append(n)
        answer.append(temp)
                
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))