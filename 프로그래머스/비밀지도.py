n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
answer = []
map1, map2 = [], []
for i in range(n):
    map1.append(str(bin(arr1[i]))[2:].zfill(n))
    map2.append(str(bin(arr2[i]))[2:].zfill(n))
for i in range(n):
    temp = ''
    for j in range(n):
        if map1[i][j] == '0' and map2[i][j] == '0':
            temp += ' '
        else:
            temp += '#'
    answer.append(temp)