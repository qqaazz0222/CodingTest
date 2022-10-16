def solution(X, Y):
    answer = ''
    X = list(X)
    Y = list(Y)
    n = list(set(X) & set(Y))
    n.sort(reverse=True)
    for i in n:
        nx = X.count(str(i))
        ny = Y.count(str(i))
        if nx >= ny:
            minN = ny
        else:
            minN = nx
        answer += str(i)*minN
    if answer == '':
        answer = '-1'
    elif answer[0] + answer[-1] == '00':
        answer = '0'
    return answer


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))
