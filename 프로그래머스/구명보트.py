def solution(people, limit):
    answer = 0
    while True:
        if people == []:
            break
        p1 = min(people)
        del people[people.index(p1)]
        people.sort(reverse=True)
        for i in people:
            if p1 + i <= limit:
                del people[people.index(i)]
                break
            answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))