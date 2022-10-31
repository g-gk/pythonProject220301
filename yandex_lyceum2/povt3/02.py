# Подбор мелодии
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


class Melody:
    def __init__(self, notes=[]):
        # self.notes = [note for note in notes]
        self.notes = notes

    def __str__(self):
        return ', '.join(str(x) for x in self.notes).capitalize()

    def append(self, note):
        self.notes.append(note)

    def replace_last(self, note):
        self.notes[-1] = note

    def remove_last(self):
        self.notes.pop()

    def clear(self):
        self.notes.clear()

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, n):
        # t = self.notes.copy()
        t = [Note(x.note, x.is_long) for x in self.notes]
        for i in range(len(t)):
            if PITCHES.index(t[i].note) + n > N - 1:
                return Melody(self.notes.copy())
            else:
                t[i].note = PITCHES[PITCHES.index(t[i].note) + n]
        return Melody(t)

    def __lshift__(self, n):
        # t = self.notes.copy()
        t = [Note(x.note, x.is_long) for x in self.notes]
        for i in range(len(t)):
            if PITCHES.index(t[i].note) - n < 0:
                return Melody(self.notes.copy())
            else:
                t[i].note = PITCHES[PITCHES.index(t[i].note) - n]
        return Melody(t)


def main():
    print('---------- Пример 1 ----------')
    melody = Melody([Note('фа'), Note('ми'), Note('ре'), Note('до'), Note('ля')])
    print(melody)
    melody.replace_last(Note('си', True))
    print(melody)
    melody.remove_last()
    print(melody)
    melody.append(Note('соль', True))
    melody.append(Note('соль', True))
    print(melody)

    print('---------- Пример 2 ----------')
    melody = Melody([Note('до'), Note('ми'), Note('соль', True)])
    print(melody, len(melody))
    print(Melody(), len(Melody()))
    melody.clear()
    print(melody, len(melody))

    print('---------- Пример 3 ----------')
    melody = Melody([Note('ля'), Note('соль'), Note('ми'), Note('до', True)])
    print(melody)
    print(Melody() >> 2)
    melody_up = melody >> 1
    melody_down = melody << 1
    melody.replace_last(Note('соль'))
    print('>> 1:', melody_up)
    print('<< 1:', melody_down)
    print(melody)


if __name__ == '__main__':
    main()
