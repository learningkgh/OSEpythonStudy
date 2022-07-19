def solution(s):
    answer = 0
    en = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,num in enumerate(en):
        if num in s:
            s=s.replace(num,str(i))
        answer = s
    return int(answer) 
