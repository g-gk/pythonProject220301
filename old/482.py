# GET
data = input().split('?')[1].split('&')
key = input()
for el in data:
    k, v = el.split('=')
    if k == key:
        print(v)
        break
