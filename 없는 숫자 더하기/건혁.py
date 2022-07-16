def solution(numbers):
    answer = 0
    checkList = list(range(0,10))
    emptyNum = list(set(checkList) - set(numbers))
    
    for i in range(len(emptyNum)):
        answer += emptyNum[i]
    
    return answer
