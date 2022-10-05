# def fact(n):
#     res = 0
#     a = 0
#     b = 1
#     if n == 1:
#         res = 1
#     else:
#         for i in range(n-1):
#             temp = b
#             b = a+b
#             a = temp
#         res = b
#     return res
# print(fact(6))

def solution(n):
    answer = 0
    a = 0
    b = 1
    if n == 1:
        answer = 1
    else:
        for i in range(n):
            temp = b
            b = a+b
            a = temp
        answer = b
    answer = answer % 1234567
    return answer

for i in range(1, 20):
    print(solution(i))
# print(solution(2000))