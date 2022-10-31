def password_level(password):
    # проверка на длину пароля
    if len(password) < 6:
        return 'Недопустимый пароль'
    # если длина парооля больше или равна 6
    else:
        # проверка содержатся ли только цифры или только буквы одного регистра
        if password.isdigit() or (password.isalpha() and password.islower()):
            return 'Ненадежный пароль'
        # проверка содержатся ли буквы разных регистров или буквы одного регистра и цифры
        elif password.isalpha() or (password.isalnum() and password.islower()) \
                or (password.isalnum() and password.isupper()):
            return 'Слабый пароль'
        # если пароль не является слабым, ненадежным и недопустимым, значит пароль надежный
        else:
            return 'Надежный пароль'


print(password_level("qwerty"))
print(password_level("123Qwerty"))
print(password_level("Qwerty"))
