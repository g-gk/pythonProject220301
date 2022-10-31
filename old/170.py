from random import choice, sample
from string import punctuation
from swift import words

swiftt = words


def generatetext():
    global swiftt
    solution_txt = list(filter(lambda x: x not in punctuation, swiftt))
    solution_txt2 = ((' '.join((sample(solution_txt, choice(range(5, 20)))))).lower()).split()
    for empty in solution_txt2:
        solution_txt2.insert(0, empty[0].upper() + empty[1:])
        break
    solution_txt2.remove(solution_txt2[1])
    for empty in solution_txt2:
        if solution_txt2.count(empty) != 1:
            del solution_txt2[' '.join(solution_txt2).rfind(empty)]
    return ' '.join(solution_txt2) + '.'


def main():
    flag = True
    Num = int(input('Введите число, сколько будет пелеберды :D : '))
    for _ in range(Num):
        while flag:
            try:
                print(generatetext())
                flag = False
            except IndexError:
                swiftt = words


if __name__ == '__main__':
    main()
