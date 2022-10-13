def solution(s):
    answer = ''
    number = ['one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']

    for i in number:
        if i in s:
            print(number.index(i)+1)


print(solution("one4seveneight"))
