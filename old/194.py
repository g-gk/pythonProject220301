import math


def d(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def distance(t):
    return math.hypot(0.7500 - t[0], 0 - t[1])


plist = [(math.cos(t) * math.cos(t) * math.cos(t),
          math.sin(t) * math.sin(t) * math.sin(t))
         for t in d(0, 2 * 3.1416, 0.01)]
dists = [round(distance(x), 4) for x in plist]
print(min(dists))
