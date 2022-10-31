# Клавиатура
n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
cnt = [0] * n
for el in p:
    cnt[el - 1] += 1
for i in range(n):
    if cnt[i] > c[i]:
        print('yes')
    else:
        print('no')
