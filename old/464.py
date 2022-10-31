# Большой колокольчик
class BigBell:
    def __init__(self):
        self.sw = True

    def sound(self):
        if self.sw:
            print('ding')
        else:
            print('dong')
        self.sw = not self.sw


# bell = BigBell()
# bell.sound()
# bell.sound()
# bell.sound()
