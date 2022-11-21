from queue import PriorityQueue


def solution(program):
    answer = [0]*10
    program.sort(key=lambda x: x[1])
    pQ = PriorityQueue()
    cur = 0

    def call_program():
        while len(program) > 0 and program[0][1] <= cur:
            pQ.put(program.pop(0))

    while len(program) > 0 or not pQ.empty():
        if pQ.empty():
            cur = program[0][1]
            call_program()
        execute = pQ.get()
        answer[execute[0]-1] += (cur-execute[1])
        cur += execute[2]
        call_program()
    return [cur] + answer


print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
# [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
# [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
