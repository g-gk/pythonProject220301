# Разреженный массив

class SparseArray:
    def __init__(self):
        self.arr = {}

    def __getitem__(self, key):
        return self.arr.get(key, 0)

    def __setitem__(self, key, value):
        self.arr[key] = value


def main():
    print('----- Пример 1 -----')
    arr = SparseArray()
    arr[1] = 10
    arr[8] = 20
    for i in range(10):
        print('arr[{}] = {}'.format(i, arr[i]))

    print('----- Пример 2 -----')
    arr = SparseArray()
    arr[10] = 123
    for i in range(8, 13):
        print('arr[{}] = {}'.format(i, arr[i]))

    print('----- Пример 3 -----')

    def print_elem(array, ind):
        print('arr[{}] = {}'.format(ind, array[ind]))

    arr = SparseArray()
    index = 1000000000
    arr[index] = 123

    print_elem(arr, index - 1)
    print_elem(arr, index)
    print_elem(arr, index + 1)
    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
