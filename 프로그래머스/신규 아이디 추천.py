def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalpha():
            pass
        elif i.isdigit():
            pass
        elif i in ["-", "_", "."]:
            pass
        else:
            new_id = new_id.replace(i, "")
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    if new_id == "":
        pass
    else:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id == "":
        pass
    else:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution(	"123_.def"))
print(solution("abcdefghijklmn.p"))