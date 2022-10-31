# Подробный список покупок
n = int(input())
ans = []
ans = [input() + ' ' + input() for _ in range(n)]
print('\n'.join(ans[::-1]))
