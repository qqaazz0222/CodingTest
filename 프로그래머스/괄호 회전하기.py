def check(s):
    res = 0
    stack = []
    for i in s:
        print(i)
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif len(stack) > 0 and (i == ')' or i == '}' or i == ']'):
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append('e')
                break
        else:
            break
        print(stack)
        if len(stack) == 0:
            res = 1
    return res


# def solution(s):
#     answer = 0
#     ls = len(s)
#     temp = 0
#     while True:
#         print(s, answer)
#         if temp == ls:
#             break
#         else:
#             stack = []
#             for i in s:

#                 if i == '(' or i == '{' or i == '[':
#                     stack.append(i)
#                 elif len(stack) != 0:
#                     if stack[-1] == i:
#                         stack.pop()
#                     else:
#                         break
#                 else:
#                     stack.append('e')
#                     break
#             if len(stack) == 0:
#                 answer += 1
#             s = s[1:] + s[0]
#             temp += 1
#     return answer


print(check("[](){}"))
print(check("}]()[{"))
print(check("[)()]"))
print(check("}}}"))
