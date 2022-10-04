def solution(n, words):
    answer = []
    round = 0
    errround = 0
    temp = words[0][0]
    print(temp)
    used = []
    for i in words:
        print(round, errround, used)
        if temp[-1] == i[0]:
            if i in used:
                errround = round
                break
            else:
                round += 1
                used.append(i)
        else:
            errround = round
            break
    answer = [errround%n, errround//n]


    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))