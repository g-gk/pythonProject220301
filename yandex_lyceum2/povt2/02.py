# Но-оты
class Note:
    def __init__(self, note, dlit=False):
        self.notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
        self.dlit_notes = ['до-о', 'ре-э', 'ми-и', 'фа-а', 'со-оль', 'ля-а', 'си-и']
        self.note = note
        self.dlit = dlit

    def __str__(self):
        if self.dlit:
            return self.dlit_notes[self.notes.index(self.note)]
        return self.note


def main():
    print('---------- Пример 1 ----------')
    do_1 = Note("до", False)
    doo = Note("до", True)
    do_2 = Note("до")
    print(do_1, doo, do_2)

    print('---------- Пример 2 ----------')
    sool = Note("соль", True)
    laa = Note("ля", True)
    print(sool, laa)


if __name__ == '__main__':
    main()
