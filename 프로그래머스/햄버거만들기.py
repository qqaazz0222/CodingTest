# def solution(ingredient):
#     answer = 0
#     stack = []
#     for i in ingredient:
#         if i == 1:
#             if len(stack) != 0:
#                 temp = stack.pop()
#                 if temp == [1, 2, 3]:
#                     answer += 1
#                 else:
#                     stack.append([1])
#             stack.append([1])
#         else:
#             if len(stack) > 0:
#                 temp = stack.pop()
#                 if len(temp) != 0:
#                     if temp[-1]+1 == i:
#                         temp += [i]
#                         stack.append(temp)
#         print(stack)
#     return answer


def solution(ing):
    answer = 0
    stack = []
    temp = ""

    return answer


print(solution([2, 1, 1, 2, 3, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
