def del_other_symbols(a):
    return a.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ') .\
        replace('?', ' ').replace(':', ' ').replace('0', ' ').replace('1', ' ') .\
        replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5', ' ') .\
        replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ')


def print_long_words(text):
    s = 'аоэиуыеёюяaeiouy'
    text = del_other_symbols(text).split()
    for elem in text:
        count = 0
        for i in elem:
            if i in s or i in s.upper():
                count += 1
        if count >= 4:
            print(elem.lower())

