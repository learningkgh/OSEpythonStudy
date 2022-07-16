import itertools

def solution(numbers):
    answer = []
    a = list(itertools.combinations(numbers, 2))
    for i in range(len(a)):
        answer.append(sum(a[i]))
    answer = list(set(answer))
    answer.sort()
    return answer
