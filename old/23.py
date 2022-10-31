# Выборки
class Selector:
    def __init__(self, arr):
        self.odds = list(filter(lambda x: x % 2, arr))
        self.evens = list(filter(lambda x: x % 2 == 0, arr))

    def get_odds(self):
        return self.odds

    def get_evens(self):
        return self.evens


# values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
# selector = Selector(values)
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, odds)))
# print(' '.join(map(str, evens)))

# values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
# selector = Selector(values)
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, odds)))
# print(' '.join(map(str, evens)))

# values = []
# selector = Selector(values)
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, odds)))
# print(' '.join(map(str, evens)))

# values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
# selector = Selector(values)
# values.clear()
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, evens)))
# print(' '.join(map(str, odds)))
#
# selector = Selector([])
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, evens)))
# print(' '.join(map(str, odds)))
#
# selector = Selector([0])
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, evens)))
# print(' '.join(map(str, odds)))
