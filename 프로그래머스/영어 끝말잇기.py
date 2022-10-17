def solution(n, words):
    answer = [0, 0]
    used = ['0']
    stack = [words[0][0]]
    round = 0
    while True:
        if round == len(words):
            break
        elif words[round] in used:
            answer[0] = round % n+1
            answer[1] = round//n+1
            break
        elif words[round][0] != stack[-1]:
            answer[0] = round % n+1
            answer[1] = round//n+1
            break
        else:
            used.append(words[round])
            stack.append(words[round][-1])
            round += 1

    return answer


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
