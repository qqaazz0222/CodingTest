def solution(queries):
    answer = []
    child = ["RR", "Rr", "Rr", "rr"]

    def back(gen, x):
        if gen == 1:
            return "Rr"
        parent = back(gen-1, x//4)
        if parent == "Rr":
            return child[x % 4]
        else:
            return parent

    for q in queries:
        n, p = q
        result = back(n, p-1)
        answer.append(result)

    return answer


print(solution([[3, 5]]))
# ["RR"]
print(solution([[3, 8], [2, 2]]))
# ["rr", "Rr"]
print(solution([[3, 1], [2, 3], [3, 9]]))
# ["RR", "Rr", "RR"]
print(solution([[4, 26]]))
# ["Rr"]
