def solution(s):
    answer = 0
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in num:
        if s.find(i) != -1:
            s = s.replace(i, str(num.index(i)))
    answer = int(s)
        
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))