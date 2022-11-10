def solution(id_list, report):
    temp_id = []
    temp = []
    for i in report:
        user = i.split(' ')
        if user[1] not in temp_id:
            temp_id.append(user[1])
        idx = temp_id.index(user[1])
        if user[0] not in temp[idx]:
            temp[idx].append(user[0])
        else:
            temp[idx].append(user[0])
    result = []
    for i in temp:
        result.append(len(i))
    return result


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]))
print(solution(["con", "ryan"], ["ryan con",
      "ryan con", "ryan con", "ryan con"]))
