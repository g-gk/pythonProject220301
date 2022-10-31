# /etc/passwd
data = []
while True:
    tmp = input()
    if tmp:
        tmp = tmp.split(':')
        data.append((tmp[0], tmp[4].split(',')[0], tmp[1]))
    else:
        break
bad_passwords = set(input().split(';'))
for user in data:
    if user[2] in bad_passwords:
        print(f'To: {user[0]}')
        print(f'{user[1]}, ваш пароль слишком простой, смените его.')
