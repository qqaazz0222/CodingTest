def solution(phone_book):
    answer = True
    while True:
        temp = []
        if len(phone_book) <= 1:
            break
        else:
            for i in phone_book[1:]:
                temp.append(i[:len(phone_book[0])])

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
