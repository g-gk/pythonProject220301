class WaitingLounge:
    def __init__(self, planet, list_destinations, volume):
        self.planet = planet
        self.list_destinations = list_destinations
        self.volume = volume

    def __lt__(self, other):
        return (len(self.list_destinations), self.volume, self.planet) < \
               (len(other.list_destinations), other.volume, other.planet)

    def __le__(self, other):
        return (len(self.list_destinations), self.volume, self.planet) <= \
               (len(other.list_destinations), other.volume, other.planet)

    def __gt__(self, other):
        return (len(self.list_destinations), self.volume, self.planet) > \
               (len(other.list_destinations), other.volume, other.planet)

    def __ge__(self, other):
        return (len(self.list_destinations), self.volume, self.planet) >= \
               (len(other.list_destinations), other.volume, other.planet)

    def __eq__(self, other):
        return (len(self.list_destinations), self.volume, self.planet) == \
               (len(other.list_destinations), other.volume, other.planet)

    def __ne__(self, other):
        return (len(self.list_destinations), self.volume, self.planet) != \
               (len(other.list_destinations), other.volume, other.planet)

    def __add__(self, other):
        planet = min(self.planet, other.planet)
        list_destinations = sorted(list(set(self.list_destinations) & set(other.list_destinations)))
        volume = self.volume + other.volume
        return WaitingLounge(planet, list_destinations, volume)

    def __isub__(self, line):
        if line in self.list_destinations:
            self.list_destinations.remove(line)
            self.volume -= len(line)
        else:
            self.list_destinations.append(line)
            self.volume += len(line)
        return self

    def __mul__(self, number):
        res = []
        for i in range(number):
            if i < len(self.list_destinations):
                res.append(
                    WaitingLounge(self.planet, [self.list_destinations[i]], self.volume // number))
            else:
                res.append(
                    WaitingLounge(self.planet, [''], self.volume // number))
        return res

    def __call__(self, number):
        return len(self.list_destinations) * self.volume // number

    def get_destinations(self):
        return self.list_destinations

    def __str__(self):
        return f'The waiting lounge on the planet {self.planet} ' \
               f'accommodates {self.volume} passengers.'

    def __repr__(self):
        s = "', '"
        return f"WaitingLounge('{self.planet}', " \
               f"['{s.join(sorted(self.list_destinations))}'], {self.volume})"
