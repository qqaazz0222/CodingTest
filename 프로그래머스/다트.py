def solution(dartResult):
    answer = 0
    for i in range(1, 10):
        dartResult = dartResult.split(str(i))
    return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))