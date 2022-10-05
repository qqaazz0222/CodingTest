import math
def solution(n,a,b):
    answer = 0
    while True:
        if a == b:
            break
        else:
            answer += 1
            a = math.ceil(a/2)
            b = math.ceil(b/2)
    return answer

print(solution(8, 4, 7))