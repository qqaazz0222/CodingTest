def solution(n, lost, reserve):
    answer = 0
    r = set(reserve) - set(lost)
    l = set(lost) - set(reserve)
    for i in r:
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)
    answer = n-len(l)
    return answer
print(solution(5, [1, 2, 4, 5], [2, 3, 4]))
print("----")
print(solution(5, [2, 4], [3]))
print("----")
print(solution(3, [3], [1]))