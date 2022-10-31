def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        while True:
            print(i, answer)
            if i[0:2] in can:
                if len(i) == 2:
                    answer += 1
                    break
                else:
                    if i[2:4] != i[0:2]:
                        i = i[2:]
                    else:
                        break
            elif i[0:3] in can:
                if len(i) == 3:
                    answer += 1
                    break
                else:
                    if i[3:6] != i[0:3]:
                        i = i[3:]
                    else:
                        break
            else:
                break
    return answer


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
