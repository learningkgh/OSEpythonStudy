def solution(left, right):
    num = 0
    answer = 0
    while left < right+1:
        for i in range(1,left+1):
            if left % i == 0:
                num += 1
        if num % 2 == 0:
            answer += left
        else:
            answer -= left
        num = 0
        left += 1

    return answer
