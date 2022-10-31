# Ним3-пасьянс
stones = [int(input()) for _ in range(3)]
while sum(stones) > 0:
    n = int(input())
    cnt = int(input())
    stones[n - 1] -= cnt
    print(*stones)
