from sys import stdin

books = [i for i in input().split('\t') if i]
print(books)
shop_price = []
for a in stdin:
    a = a.split('\n')[0].split('\t')
    x = (a[0], sum([int(i) for i in a[1:]]), a[1:])
    shop_price.append(x)
shop = min(shop_price, key=lambda x: x[1])
print(shop[0])
print('\n'.join(['\t'.join(i) for i in zip(books, shop[-1])]))
