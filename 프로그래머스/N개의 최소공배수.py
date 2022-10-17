def solution(arr):
    answer = 0
    a = arr.pop()
    b = 0
    while True:
        if len(arr) == 0:
            break
        else:
            b = arr.pop()
            for i in range(max(a, b), a*b+1):
                if i % a == 0 and i % b == 0:
                    a = i
    answer = a
    return answer


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
