# Шеренга
# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось
# определить своё место в строю. Помогите ему это сделать.
a = list(map(int, input().split()))
x = int(input())
i = 0
while i < len(a) and x <= a[i]:
    i += 1
print(i + 1)