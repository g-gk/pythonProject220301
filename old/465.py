# Самые короткие и самые длинные слова
class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, text):
        self.words += text.split()

    def shortest_words(self):
        if self.words:
            mn = len(min(self.words, key=len))
            return sorted(x for x in self.words if len(x) == mn)
        return []

    def longest_words(self):
        if self.words:
            mx = len(max(self.words, key=len))
            return sorted(set(x for x in self.words if len(x) == mx))
        return []


def main():
    print('Пример 1')
    finder = MinMaxWordFinder()
    finder.add_sentence('hello abc world')
    finder.add_sentence('def asdf qwert')
    print(' '.join(finder.shortest_words()))
    print(' '.join(finder.longest_words()))
    print('Пример 2')
    finder = MinMaxWordFinder()
    finder.add_sentence('hello')
    finder.add_sentence('abc')
    finder.add_sentence('world')
    finder.add_sentence('def')
    finder.add_sentence('asdf')
    finder.add_sentence('qwert')
    print(' '.join(finder.shortest_words()))
    print(' '.join(finder.longest_words()))
    print('Пример 3')
    finder = MinMaxWordFinder()
    finder.add_sentence('hello')
    finder.add_sentence('  abc     def    ')
    finder.add_sentence('world')
    finder.add_sentence('            abc          ')
    finder.add_sentence('asdf')
    finder.add_sentence('qwert')
    print(' '.join(finder.shortest_words()))
    print(' '.join(finder.longest_words()))
    print('Пример 4')
    finder = MinMaxWordFinder()
    print(' '.join(finder.shortest_words()))
    print(' '.join(finder.longest_words()))

    finder = MinMaxWordFinder()
    print(' '.join(finder.longest_words()))
    print(' '.join(finder.shortest_words()))


if __name__ == '__main__':
    main()
