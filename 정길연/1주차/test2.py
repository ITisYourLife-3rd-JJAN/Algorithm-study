def findRange(num):
    nstr = str(num)

    if nstr[0] != '9':
        max_str = nstr.replace(nstr[0], '9')
    else :      # 가장 큰 자리 수가 9일 경우.. 일단 9을 다 뺸다.
        tmp = nstr.replace('9', '')
        if len(tmp) == 0: 
            max_str = nstr
        else : 
            max_str = nstr.replace(tmp[0], '9')

    
    if nstr[0] != '1':
        min_str = nstr.replace(nstr[0], '1')
    else:   # 가장 큰 자리 수가 1일 경우.. 일단 1을 다 빼고, 가장 큰 자리수에 있는 수 0으로
        tmp = nstr.replace('1', '')
        if len(tmp) == 0: 
            min_str = nstr
        else : 
            min_str = nstr.replace(tmp[0], '0')
    
    return int(max_str) - int(min_str)
        

            

print(findRange(99902))