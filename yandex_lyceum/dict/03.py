# Предсказание погоды с памятью
today = input()
p = float(input())
q = float(input())
n = int(input())
d = 1
if today == 'ясно':
    prob = [p, 1 - p]
elif today == 'пасмурно':
    prob = [1 - q, q]
for d in range(n - 1):
    prob = [max(prob[0] * p, prob[1] * (1 - q)),
            max(prob[0] * (1 - p), prob[1] * q)]
if prob[0] > prob[1]:
    print('ясно')
    print(prob[0])
elif prob[1] > prob[0]:
    print('пасмурно')
    print(prob[1])
else:
    print('равновероятно')
    print(prob[0])
