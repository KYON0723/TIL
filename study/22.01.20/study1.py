def is_pal_while(word):
    cnt = 0
    i = 0
    j = -1

    for k in word:
        cnt += 1

    while i < cnt:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1

    return True