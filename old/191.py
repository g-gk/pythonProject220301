def password_level(password):
    s = '0123456789'
    if len(password) < 6:
        return 'Недопустимый пароль'
    if password.isalpha():
        if password.lower() == password or password.upper() == password:
            return 'Ненадежный пароль'
        return 'Слабый пароль'
    if password.isdigit():
        return 'Ненадежный пароль'
    password = list(password)
    d = ''
    for i in password:
        if i not in s:
            d += i
    if (d.upper() == d or d.lower() == d) and len(d) != len(password):
        return 'Слабый пароль'
    return 'Надежный пароль'


print(password_level("qwerty"))
print(password_level("123Qwerty"))
print(password_level("Qwerty"))
