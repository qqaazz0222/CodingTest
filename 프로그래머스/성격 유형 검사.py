def solution(survey, choices):
    answer = ''
    scoreIdx = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    scoreNum = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(survey)):
        temp = choices[i] - 4
        if temp > 0:
            scoreNum[scoreIdx.index(survey[i][1])] += temp
        elif temp < 0:
            scoreNum[scoreIdx.index(survey[i][0])] -= temp
    for i in range(0, 7, 2):
        if scoreNum[i] >= scoreNum[i+1]:
            answer += scoreIdx[i]
        else:
            answer += scoreIdx[i+1]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
