# I. Клавиатура
s = input()
s1 = ''

for c in s:
    if c != ' ':
        s1 += c

words = []
w = s1[0]
for c in s1[1:]:
    if c.isupper() and w.isupper() or c.islower() and w.islower():
        w += c
    else:
        words.append(w)
        w = c
words.append(w)

cnt_up, cnt_low = 0, 0
for w in words:
    if w.isupper():
        cnt_up += 1
    elif w.islower():
        cnt_low += 1

if cnt_up > cnt_low:
    words1 = []
    for w in words:
        if w.isupper():
            words1.append(w.lower())
        elif w.islower():
            words1.append(w.upper())
    words = words1

words.append('')
cnt = 0
for i in range(len(words)):
    if words[i].isupper():
        if len(words[i]) == 1:
            cnt += 1
        elif len(words[i]) == 2:
            cnt += 2
        elif len(words[i]) == 3:
            if words[i + 1]:
                cnt += 3
            else:
                cnt += 2
        elif len(words[i]) >= 4:
            if words[i + 1]:
                cnt += 4
            else:
                cnt += 2
print(len(s) + cnt)
