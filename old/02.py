from random import sample, randrange, choice

planets = int(input())
tmp = input().split()
letters = list(tmp[0])
len_name = int(tmp[1])
stars = input().split('; ')
t1, t2 = map(float, input().split())
climats = input().split(', ')
orb1, orb2 = map(int, input().split())
names_of_planets = set()
while len(names_of_planets) < planets:
    names_of_planets.add(''.join(choice(letters) for i in range(len_name)))
names_of_planets = list(names_of_planets)
naklons = sample(range(orb1, orb2 + 1, 2), planets)
for i in range(planets):
    print(f'Planet {names_of_planets[i]} {i + 1} from {choice(stars)}.')
    prod = randrange(t1 * 10, t2 * 10 + 1)
    print(f'Day {prod // 10}.{prod % 10}, climate {choice(climats)},',
          f'the inclination of the orbit {naklons[i]}.')
