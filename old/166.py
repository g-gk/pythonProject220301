def mirror(arr):
    mirrored_part = str(arr[::-1])
    # заменяем функцию replace, которая переворачивает сам список, но ничего при этом не возвращает
    # на обратный перебор списка, а также преобразовываем это в строку
    mirrored_part = mirrored_part.replace('[', '')
    mirrored_part = mirrored_part.replace(']', '')
    mirrored_part = mirrored_part.replace(',', '')
    # удаляем из строки квадратные скобки и запятые
    arr.append(mirrored_part)
    # до этого создавалась копия списка arr, в которую добавлялась
    # новая переменная, когда в нужный список ничего не добавлялось.
    # С функцией append переменная mirrored_part добавляется напрямую в нужный список arr


arr = [1, 2]
mirror(arr)
print(arr)
