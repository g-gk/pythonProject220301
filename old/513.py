# Слова для кадавра
def ok(w1, w2):
    gl = 'уеёыаоэяию'
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if w1[i] == '0' and w2[i] not in gl or w1[i] == '1' and w2[i] in gl:
            return False
    return True


w1 = input()
ans = []
if '*' not in w1:
    w = input()
    while w:
        if ok(w1, w):
            ans += [w]
        w = input()
else:
    w2, w3 = w1.split('*')
    w = input()
    while w:
        f1 = len(w) >= len(w1) - 1
        f2 = ok(w2, w[:len(w2)])
        f3 = True if not w3 else ok(w3, w[-len(w3):])
        if f1 and f2 and f3:
            ans += [w]
        w = input()
if ans:
    print('\n'.join(ans))
else:
    print('Есть нечего, значить!')
