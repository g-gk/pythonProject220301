def eratosthenes(n):
    arr = list(range(n + 1))
    p = 1
    while (True):
        f = 0
        j = 2
        while (j <= n):
            if (arr[j] != 0) & (arr[j] > p):
                p = arr[j]
                i = j + 1
                while (i <= n):
                    if (arr[i] != 0) & (arr[i] % p == 0):
                        print(arr[i], end=' ')
                        arr[i] = 0
                        f = 1
                    else:
                        i += 1
            else:
                j += 1
        if (f == 0):
            break


eratosthenes(15)
