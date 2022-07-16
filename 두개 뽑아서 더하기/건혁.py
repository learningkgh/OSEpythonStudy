
from itertools import combinations
def solution(numbers):
    ans = []
    numSum = list(combinations(numbers, 2))
    for i in range(len(numSum)):
        ans.append(sum(numSum[i]))         
    answer = list(set(ans))
    answer.sort()
    return answer
