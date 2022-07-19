def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        qNum = 0
        for j in range(1, i + 1):
            if i % j == 0:
                qNum += 1
            else:
                pass
        if qNum % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
