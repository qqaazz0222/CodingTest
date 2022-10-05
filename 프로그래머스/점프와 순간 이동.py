def solution(n):
    ans = bin(n).count('1')
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))