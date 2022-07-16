from itertools import combinations, permutations

def solution(numbers):
    numbers.sort()
    answer = []
    combi = list(combinations(numbers, 2))
    for i,j in combi:
        answer.append(i+j)
    answer = list(set(answer))
    answer.sort()
    return answer
