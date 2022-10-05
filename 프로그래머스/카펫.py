def solution(brown, yellow):
    answer = []
    temp = []
    for i in range(1, brown+yellow):
        if (brown+yellow)%i==0:
            temp.append(i)
    for x in temp:
        y = int((brown+yellow)/x)
        if ((brown+yellow)-(2*x)-(2*y)+4 == yellow):
            answer = [max(x, y), min(x, y)]
            break
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))