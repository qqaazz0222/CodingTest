def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        if (can[0]*2 in i) or (can[1]*2 in i) or (can[2]*2 in i) or (can[3]*2 in i):
            continue
        else:
            while True:
                if (can[0] not in i) and (can[1] not in i) and (can[2] not in i) and (can[3] not in i):
                    if len(i) == 0:
                        answer += 1
                    break
                else:
                    if can[0] in i:
                        i = i.replace(can[0], '')
                    elif can[1] in i:
                        i = i.replace(can[1], '')
                    elif can[2] in i:
                        i = i.replace(can[2], '')
                    elif can[3] in i:
                        i = i.replace(can[3], '')
    return answer


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
