def print_long_words(text):
    text = text.lower()
    for i in text:
        if i not in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
            text = text.replace(i, ' ')
    a = text.split()
    for j in a:
        b = 0
        for k in j:
            b += 1 if k in 'аоэиуыеёюяaeiouy' else 0
        if b >= 4:
            print(j)


print_long_words(
    'Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')
