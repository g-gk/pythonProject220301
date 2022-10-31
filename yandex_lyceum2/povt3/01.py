# Интервалы и транспонирование
N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[PITCHES.index(self.note)]
        return self.note

    def __lt__(self, other):
        return PITCHES.index(self.note) < PITCHES.index(other.note)

    def __le__(self, other):
        return PITCHES.index(self.note) <= PITCHES.index(other.note)

    def __eq__(self, other):
        return self.note == other.note

    def __ne__(self, other):
        return self.note != other.note

    def __gt__(self, other):
        return PITCHES.index(self.note) > PITCHES.index(other.note)

    def __ge__(self, other):
        return PITCHES.index(self.note) >= PITCHES.index(other.note)

    def __rshift__(self, n):
        note = PITCHES[(PITCHES.index(self.note) + n) % N]
        return Note(note, self.is_long)

    def __lshift__(self, n):
        note = PITCHES[(PITCHES.index(self.note) - n) % N]
        return Note(note, self.is_long)

    def get_interval(self, other):
        return INTERVALS[abs(PITCHES.index(self.note) - PITCHES.index(other.note))]


class LoudNote(Note):
    def __init__(self, note, is_long=False):
        super().__init__(note, is_long)

    def __str__(self):
        return Note.__str__(self).upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        super().__init__(note, is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        super().__init__(note, is_long)
        self.octave = octave

    def __str__(self):
        return Note.__str__(self) + f' ({self.octave})'


def main():
    print('---------- Пример 1 ----------')
    fa1 = Note("фа", True)
    fa2 = Note("фа")
    print(fa1 == fa2)
    print(fa1 > fa2)
    print(fa1 < fa2)
    print(fa1 <= fa2)

    la = Note("ля", True)
    print(fa1 < la)

    print('---------- Пример 2 ----------')
    fa2 = Note("фа")
    la = Note("ля", True)
    print(la >> 1)
    print(la >> 2)
    x = fa2 << 4
    print(x)

    print('---------- Пример 3 ----------')
    fa1 = Note("фа", True)
    fa2 = Note("фа")
    la = Note("ля", True)
    print(la.get_interval(fa1))
    print(fa1.get_interval(fa2))
    print(fa1.get_interval(Note('си')))


if __name__ == '__main__':
    main()
