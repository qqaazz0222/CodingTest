import collections


def solution(input_string):
    answer = ''
    temp = []
    sH = collections.defaultdict(int)
    prev = None
    for cur in input_string:
        if prev != cur:
            sH[cur] += 1
        prev = cur
    for x in sH:
        if sH[x] >= 2:
            temp.append(x)
    if len(temp) == 0:
        answer = "N"
    else:
        temp.sort()
        for s in temp:
            answer += s
    return answer


print(solution("edeaaabbccd"))
# "de"
print(solution("eeddee"))
# "e"
print(solution("string"))
# "N"
print(solution("zbzbz"))
# "bz"
