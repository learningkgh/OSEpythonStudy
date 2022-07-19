def solution(new_id):
    answer=''
    new_id = new_id.lower()
    answer = new_id.replace('~','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('=','').replace('+','').replace('[','').replace('{','').replace(']','').replace('}','').replace(':','').replace('?','').replace(',','').replace('?','').replace(',','').replace('<','').replace('>','').replace('/','')

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer.strip(.)
    return answer
