class ReversedList:
    def __init__(self, args):
        self.args = args[::-1]

    def __len__(self):
        return len(self.args)

    def __getitem__(self, item):
        return self.args[item]


# rl = ReversedList([10, 20, 30])
# for i in range(len(rl)):
#     print(rl[i])
#
# rl = ReversedList([])
# print(len(rl))
#
# rl = ReversedList([10])
# print(len(rl))
# print(rl[0])
