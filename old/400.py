for gol in range(100, 1000):
    fb = gol ** 2
    sg = str(gol)
    sf = str(fb)
    if (sg[-2:] == sf[-2:] and len(sg) == len(set(sg)) == 3 and len(sf) == len(set(sf)) == 6 and
        len(set(sg[0] + sf))) == 7:
        print(sg, sf)
