def is_pal_recursive(word):
    cnt = 0
    for i in word:
        cnt += 1
    
    if cnt < 2:
        return True
    
    if word[0] != word[-1]:
        return False
    
    else:
        nw = word[1:-1]
        return is_pal_recursive(nw)
        
    return True