n = int(input())
text = 'НЕТ'
for i in range(n):
    k = len(input())
    if k % 3 == 0 and text == 'НЕТ':
        text = str(i + 1)
print(text, end='')
