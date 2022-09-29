# def solution(id_list, report, k):
#     answer = []
#     data = {}
#     lock = []
#     return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
answer = []
report_list = {}
count = {}
for i in id_list:
    report_list[i] = []
    count[i] = 0
for i in report:
    u1, u2 = map(str, i.split(" "))
    if u2 not in report_list[u1]:
        report_list[u1].append(u2)
        count[u2] += 1
for i in report_list:
    temp = 0
    for j in report_list[i]:
        if count[j] >= k:
            temp += 1
    answer.append(temp)
print(answer)