# Больше нот, хороших и разных
PITCHES = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']


class Note:
    def __init__(self, note, is_long=False):
        self.dlit_notes = ['до-о', 'ре-э', 'ми-и', 'фа-а', 'со-оль', 'ля-а', 'си-и']
        self.note = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return self.dlit_notes[PITCHES.index(self.note)]
        return self.note


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
    print(Note("соль"))

    print(LoudNote(PITCHES[4]))
    print(LoudNote("си", is_long=True))

    print(DefaultNote("ми"))
    print(DefaultNote())
    print(DefaultNote(is_long=True))

    print(NoteWithOctave("ре", "первая октава"))
    print(NoteWithOctave("ля", "малая октава", is_long=True))

    print('---------- Пример 2 ----------')


if __name__ == '__main__':
    main()
