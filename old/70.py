# Сумматоры - 2
class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        res = 0
        for i in range(1, n + 1):
            res += self.transform(i)
        return res


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)


# N = 2
# print(Summator().sum(N))
# print(N * (N + 1) / 2)
