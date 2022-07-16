def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))     # 잃어버린 수 - 추가분 수
    reserveN = list(set(reserve) - set(lost))  # 추가분 수 - 잃어버린 수 
    lostN.sort()                               # lostN 정렬
    for l in lostN:                            # reserved = 나눠주고 난 수로 바꾸기
        for x in range(l-1, l+2):              
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    answer = n - len(lostN) + reserved
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))