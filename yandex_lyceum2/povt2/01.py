# Ноты
class Note:
    def __init__(self, note):
        self.note = note

    def play(self):
        print(self.note)


def main():
    do = Note("до")
    sol = Note("соль")
    sol.play()
    do.play()


if __name__ == '__main__':
    main()
