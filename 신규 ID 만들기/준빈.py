import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id) # 2단계
    new_id = re.sub(r'(([.])\2+)', '.', new_id) # 3단계
    new_id = new_id.strip('.') # 4단계
    
    if new_id == '': new_id = 'a' # 5단계
    
    if len(new_id) > 15: # 6단계
        new_id = new_id[:15]
        if new_id[-1] =='.':
            new_id = new_id.rstrip('.')
    else: pass
    
    if len(new_id) < 3: # 7단계
        while len(new_id) <= 3:
            for i in range(2):
                new_id += new_id[-1] * i
            if len(new_id) == 3:
                break
                
    return new_id
