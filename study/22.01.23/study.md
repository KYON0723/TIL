```python
def max_score(scores):
    mx_sc = 0

    for i in scores:
        if i > mx_sc:
            mx_sc = i

    return mx_sc


def over(scores):
    cnt = 0

    for i in scores:
        if i >= 60:
            cnt += 1

    return cnt


def menu_count(restorant):
    cnt = 0

    for i in restorant.get('menus'):
        cnt += 1

    return cnt

def turn(temperatures):
    maximun = []
    minimun = []

    for i in temperatures:
        maximun.append(i[0])
        minimun.append(i[1])

    result = {
        'maximun' : maximun,
        'minimun' : minimun
    }

    return result


def is_user_data_valid(user_data):
    id = user_data.get('id')
    pw = user_data.get('pw')

    if id == '' or pw == '':
        return False

    else:
        return True


def is_id_valid(user_data):
    id = user_data.get('id')

    last = id[-1:]

    for i in range(10):
        if str(i) == last:
            return True

    return False

```

