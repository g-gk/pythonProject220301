d = {}
n = int(input())  # Получение количества исходных слов
for i in range(n):
    e = input().lower()
    s = "".join(sorted(e))
    d[s] = d.get(s, set())
    d[s].add(e)  # Добавление слова в словарь, если его там нет
new_words = [" ".join(sorted(i)) for i in d.values() if len(i) > 1]  # Создание спика анаграмм
print("\n".join(sorted(new_words)))  # Сортировка и печать списка анаграмм
