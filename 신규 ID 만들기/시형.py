def solution(new_id):
    answer = ''
    
    new_id.lower() #  step 1 대문자 -> 소문자 변환
    
    for ch in new_id: # step 2   소문자, 숫자, '-', '_', '.' 제외 문자 삭제
     if ch.isalpha() or ch.isdigit() or ch in ['-', '_', '.']: # isalpha()-> 소문자
        answer += ch                                           # isdigit()-> 숫자
        
    while '..' in answer: # step 3 '..' -> '.'
        answer = answer.replace('..', '.')
        
    answer = answer.strip('.') # step 4 양 끝에 '.'이 있으면 삭제
    
    answer = 'a' if len(answer) == 0 else answer[:15]  # step 5, 6 / 빈공간에 'a' / 16개 이상이면 뒤 삭제
    answer.rstrip('.') # step 6_2 오른쪽 끝에 '.'이 있으면 삭제 
    
    while len(answer) < 3: # step 7 answer이 3글자 미만이면 마지막 글자 반복주기
        answer += answer[-1]

    return answer
