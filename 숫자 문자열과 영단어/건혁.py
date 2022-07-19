def solution(s):
    numNames = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    link = zip(numNames, num)

    for i, (a, b) in enumerate(link):
        s = s.replace(a, str(b))
    answer = int(s)
    return answer
