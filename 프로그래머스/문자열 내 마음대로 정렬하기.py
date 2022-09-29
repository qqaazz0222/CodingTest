def solution(strings, n):
    answer = []
    temp = []
    for i in strings:
        temp.append(i[n]+i)
    temp.sort()
    for i in temp:
        answer.append(i[1:])
    return answer

print(solution(["abce", "abcd", "cdx"], 2))