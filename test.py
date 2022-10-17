def solution(n):
    answer = 1
    temp = 1
    while True:
        if temp >= n:
            break
        else:
            temp *= answer
            answer += 1

    return answer


print(solution(3628800))
print(solution(7))
