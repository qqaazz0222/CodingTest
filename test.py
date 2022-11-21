from collections import deque


def solution(priorities, location):
    answer = 0
    print_stack = deque(priorities)
    job_stack = deque(x for x in range(len(priorities)))
    priority = print_stack.popleft()
    job = job_stack.popleft()
    while print_stack:
        if job < max(print_stack):
            print_stack.append(priority)
            job_stack.append(job)
        else:
            answer += 1
            if (job == location):
                return answer
        priority = print_stack.popleft()
        job = job_stack.popleft()
    return answer


print(solution([2, 1, 3, 2], 2))
print("--------------------------------")
print(solution([1, 1, 9, 1, 1, 1], 0))
