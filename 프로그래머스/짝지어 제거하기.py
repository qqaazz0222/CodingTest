def solution(s):
    answer = 0
    while True:
        if len(s) <= 2:
            break
        else:
            temp = ''
            for i in s:
                if temp == i:
                    s = s.replace(i*2, '')
                else:
                    temp = i
    temp = s[0]
    for i in s:
        if temp == i:
            answer = 1
        else:
            answer = 0
            break
    return answer

# print(solution("baabaa"))
print(solution("cdcd"))
