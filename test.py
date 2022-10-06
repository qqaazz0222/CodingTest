def solution(str1, str2):
    answer = 2
    print(str1.find(str2))
    if str1.find(str2) == 0:
        answer = 1
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))