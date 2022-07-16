def solution(n, lost, reserve):
    people = n
    lostSet = set(lost)
    reserveSet = set(reserve)
    
    overlapN = list(lostSet.intersection(reserveSet))
    
    for i in overlapN:
        reserve.remove(i)
        lost.remove(i)
    lost.sort()
    reserve.sort()
    
    for i in range(len(reserve)):
        if len(lost) == 0:
            break
        else:
            for j in range(len(lost)):
                reserveCheck = [reserve[i]-1, reserve[i], reserve[i]+1]
                if lost[j] in reserveCheck:
                    lost.remove(lost[j])
                    break
    answer = people - len(lost)
    return answer
