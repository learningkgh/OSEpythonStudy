import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)
    
    # 3단계
    new_id = re.sub(r"[^a-z0-9-_][.]+",".",new_id)
    # 4단계
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id.replace(new_id[0],"",1)
        elif new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]
    
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    
    # 6단계
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
    
    # 7단계
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    return new_id
