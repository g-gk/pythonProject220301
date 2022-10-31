def password_level(password):
    G = "0123456789"
    H1 = H2 = H3 = False
    if len(password) < 6:
        s = "Недопустимый пароль"
        return s
    elif password.isdigit():
        s = "Ненадежный пароль"
        return s
    for i in password:
        if i.isupper():
            H1 = True
        elif i in G:
            H3 = True
        elif i.islower():
            H2 = True
    if H1 * H2 * H3:
        s = "Надежный пароль"
    elif H1 ^ H2 and not H3:
        s = "Ненадежный пароль"
    else:
        s = "Слабый пароль"
    return s


print(password_level("qwerty"))
print(password_level("123Qwerty"))
print(password_level("Qwerty"))
