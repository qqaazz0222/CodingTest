def solution(queue1, queue2):
    answer = 0
    t1, t2 = 0, 0
    for i in queue1:
        t1 += i
    for i in queue2:
        t2 += i
    if (t1 + t2) % 2 != 0:
        answer = -1
    else:
        if t1 == t2:
            answer += 1
        elif t1 < t2:

        print("123")
    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
