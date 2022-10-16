def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for l in range(j+1, len(number)):
                if number[i] + number[j] + number[l] == 0:
                    answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))
