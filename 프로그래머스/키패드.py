def solution(numbers, hand):
    answer = ''
    hl, hr = [1, 4], [3, 4]
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            hl = [1,i//3+1]
        elif i in [3, 6, 9]:
            answer += "R"
            hr = [3,i//3]
        else:
            if i == 0:
                i = 11
            temp = [2, i//3+1]
            disl = abs(temp[0]-hl[0]) + abs(temp[1]-hl[1])
            disr = abs(temp[0]-hr[0]) + abs(temp[1]-hr[1])
            if disl < disr:
                answer += "L"
                hl = [2, i//3+1]
            elif disl > disr:
                answer += "R"
                hr = [2, i//3+1]
            else:
                if hand == "left":
                    answer += "L"
                    hl = [2, i//3+1]
                else:
                    answer += "R"
                    hr = [2, i//3+1]
        print(i,[2, i//3+1], hl, hr, answer[-1])
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))