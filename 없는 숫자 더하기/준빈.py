def solution(numbers):
    numbers.sort()
    l = [0,1,2,3,4,5,6,7,8,9]
    a = set(l) - set(numbers)
    answer = sum(a)
    return answer
