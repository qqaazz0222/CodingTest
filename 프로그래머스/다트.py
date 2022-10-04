def solution(dartResult):
    answer = 0
    multi = ['S', 'D', 'T']
    bonus = ['*', '#']
    templist = []
    temp = ''
    for i in dartResult:
        if i in multi:
            templist.append(int(temp)**(multi.index(i)+1))
            temp = ''
        elif i in bonus:
            if i == '*':
                if len(templist) > 1:
                    templist[-1] *= 2
                    templist[-2] *= 2
                else:
                    templist[-1] *= 2
            else:
                templist[-1] = -templist[-1]
        else:
            temp += i
    for i in templist:
        answer += i
    return answer

print(solution("1S2D*3T"))
print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))