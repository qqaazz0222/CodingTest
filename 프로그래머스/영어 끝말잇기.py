def solution(n, words):
    answer = []
    round = 0
    last = words[0][0]
    used = []
    while True:
        # print(round, words[round])
        if last != words[round][0]:
            # print("end")
            break
        else:
            # print(used)
            if words[round] in used:
                # print("end")
                break
            else:
                used.append(words[round])
                last = words[round][-1]
        round += 1
    if round == len(words):
        answer = [0,0]
    else:
        answer = [round%3+1,round//3+1]
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))