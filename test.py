s = input()
i = {}
d = {}
state = False
for i in range(len(s)):
    if d.get(s[i]) == None:
        d[s[i]] = 1
    else:
        d[s[i]] += 1
for i in d:
    d[i]
if state:
    answer = 'abc'
else:
    answer = 'N'
print(d)
print(answer)