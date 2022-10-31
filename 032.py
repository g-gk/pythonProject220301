for a1 in range(2024):
    for a2 in range(a1 + 1, 2024 - a1):
        for a3 in range(a2 + 1, 2024 - a1 - a2):
            for a4 in range(a3 + 1, 2024 - a1 - a2 - a3):
                for a5 in range(a4 + 1, 2024 - a1 - a2 - a3 - a4):
                    for a6 in range(a5 + 1, 2024 - a1 - a2 - a3 - a4 - a5):
                        a = [a1, a2, a3, a4, a5, a6]
                        if len(set(a)) == 6 and sum(a) in (2022, 2023):
                            print(*a)
