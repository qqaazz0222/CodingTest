def solution(lottos, win_nums):
    n_zero = lottos.count(0)
    n_cor = 0
    for i in win_nums:
        for j in lottos:
            if i == j:
                n_cor += 1
    print(n_cor, n_zero)
    if (n_cor == 0) and (n_zero == 0):
        answer = [6, 6]
    elif n_cor == 0:
        answer = [6 - n_zero + 1, 6]
    else:
        answer = [6 - (n_cor + n_zero) + 1, 6 - n_cor + 1]
    return answer

print(solution([7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6]))