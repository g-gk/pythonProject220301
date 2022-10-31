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

# words.append('')
cnt = 0
up = False
for i in range(len(words)):
    if up:
        if words[i].islower():
            if len(words[i]) == 1:
                cnt += 1
            elif len(words[i]) == 2:
                cnt += 2
            elif len(words[i]) == 3:
                cnt += 3
            elif len(words[i]) > 3:
                cnt += 2
                up = False
    else:
        if words[i].isupper():
            if len(words[i]) == 1:
                cnt += 1
            elif len(words[i]) == 2:
                cnt += 2
            elif len(words[i]) == 3:
                cnt += 3
            elif len(words[i]) > 3:
                cnt += 2
                up = True
print(len(s) + cnt)
