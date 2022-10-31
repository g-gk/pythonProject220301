dict_word = [i.lower() for i in input().split(' ')]
s = input().split(' ')


def is_disleksion(w1, w2):
    return sorted(list(w1.lower())) == sorted(list(w2.lower()))


# print(is_disleksion('КОТ', 'ток'))


def is_dis_from_dict(w1):
    if w1.lower() not in dict_word:
        dict_word.append(w1.lower())
    count = 0
    for w in dict_word:
        if is_disleksion(w1, w):
            count += 1
        if count > 1:
            return True
    return False


res = ''
for w in s:
    if res:
        res += ' '
    if is_dis_from_dict(w):
        res += '#' * len(w)
    else:
        res += w.lower()
print(res)
