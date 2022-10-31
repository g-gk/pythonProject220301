# Масштабирование
n = int(input())
m = int(input())
a = []
for i in range(n):
    line = input()
    if i % 2 == 0:
        print(line[::2])
